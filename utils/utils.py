import os
from matplotlib import pyplot as plt
import numpy as np
import itertools
from typing import List, Union, Tuple, Optional
from eolearn.core import EOPatch
from shapely.geometry import Polygon, MultiPolygon
from matplotlib import patches, patheffects
from datetime import datetime

from eolearn.io import ImportFromTiff

from logging import Logger
logger = Logger(__file__)


def get_extent(eopatch: EOPatch) -> Tuple[float, float, float, float]:
    """
    Calculate the extent (bounds) of the patch.

    Parameters
    ----------
    eopatch: EOPatch for which the extent is calculated.

    Returns The list of EOPatch bounds (min_x, max_x, min_y, max_y)
    -------
    """
    return eopatch.bbox.min_x, eopatch.bbox.max_x, eopatch.bbox.min_y, eopatch.bbox.max_y


def draw_outline(o, lw, foreground='black'):
    """
    Adds outline to the matplotlib patch.

    Parameters
    ----------
    o:
    lw: Linewidth
    foreground

    Returns
    -------
    """
    o.set_path_effects([patheffects.Stroke(linewidth=lw, foreground=foreground), patheffects.Normal()])


def draw_poly(ax, poly: Union[Polygon, MultiPolygon], color: str = 'r', lw: int = 2, outline: bool = True):
    """
    Draws a polygon or multipolygon onto an axes.

    Parameters
    ----------
    ax: Matplotlib Axes on which to plot on
    poly: Polygon or Multipolygons to plot
    color: Color of the plotted polygon
    lw: Line width of the plot
    outline: Should the polygon be outlined

    Returns None
    -------

    """
    if isinstance(poly, MultiPolygon):
        polys = list(poly)
    else:
        polys = [poly]
    for poly in polys:
        if poly is None:
            logger.warning("One of the polygons is None.")
            break
        if poly.exterior is None:
            logger.warning("One of the polygons has not exterior.")
            break

        x, y = poly.exterior.coords.xy
        xy = np.moveaxis(np.array([x, y]), 0, -1)
        patch = ax.add_patch(patches.Polygon(xy, closed=True, edgecolor=color, fill=False, lw=lw))

    if outline:
        draw_outline(patch, 4)


def draw_bbox(ax, eopatch: EOPatch, color: str = 'r', lw: int = 2, outline: bool = True):
    """
    Plots an EOPatch bounding box onto a matplotlib axes.
    Parameters
    ----------
    ax: Matplotlib axes on which to plot.
    eopatch: EOPatch with BBOx
    color: Color of the BBOX plot.
    lw: Line width.
    outline: Should the plot be additionally outlined.

    Returns None
    -------

    """
    bbox_poly = eopatch.bbox.get_polygon()
    draw_poly(ax, Polygon(bbox_poly), color=color, lw=lw, outline=outline)


def draw_feature(ax, eopatch: EOPatch, time_idx: Union[List[int], int, None], feature: tuple, grid: bool = True, band: int = None, interpolation: str = 'none',
              vmin: int = 0, vmax: int = 1, alpha: float = 1.0, cmap=plt.cm.viridis):
    """
    Draws an EOPatch feature.
    Parameters
    ----------
    ax: Matplotlib axes on which to plot on
    eopatch: EOPatch for which to plot the mask:
    time_idx: Time index of the mask. If int, single time index of the mask feature, if List[int] multiple masks for
    each time index. If None, plot mask_timeless.
    feature: Tuple defining feature to plot, e.g. (FeatureType.DATA, 'DATA').
    grid: Show grid on plot:
    interpolation: Interpolation used by imshow
    vmin: Minimum value (for mask visualization)
    vmax: Maximum value (for mask visualization)
    alpha: Transparency of the mask
    Returns
    -------

    """

    def _show_single_ts(axis, img, ts):
        fh = axis.imshow(img, extent=get_extent(eopatch), vmin=vmin, vmax=vmax, alpha=alpha, cmap=cmap, interpolation=interpolation)
        if grid:
            axis.grid()
        title = f'{feature[1]} {eopatch.timestamp[ts]}' if ts is not None else f'{feature[1]}'
        axis.set_title(title)
        return fh

    if time_idx is None:
        image = eopatch[feature][..., band] if band is not None else eopatch[feature].squeeze() 
        return _show_single_ts(ax, image, time_idx)
    elif isinstance(time_idx, int):
        image = eopatch[feature][time_idx][..., band] if band is not None else eopatch[feature][time_idx].squeeze()
        return _show_single_ts(ax, image, time_idx)
    elif isinstance(time_idx, list):
        for i, tidx in enumerate(time_idx):
            image = eopatch[feature][tidx][..., band] if band is not None else eopatch[feature][tidx].squeeze()
            fh = _show_single_ts(ax[i], image, tidx)
        return fh
    
    
def draw_true_color(ax: plt.axes, eopatch: EOPatch, time_idx: Union[List[int], int],
                    feature_name='BANDS-S2-L2A',
                    bands: Tuple[int] = (3, 2, 1),
                    factor: int = 3.5,
                    grid: bool = True):
    """
    Visualization of the bands in the EOPatch.
    Parameters
    ----------
    ax: Axis on which to plot
    eopatch: EOPatch to visualize.
    time_idx: Single timestamp or multiple timestamps.
    feature_name: Name of the feature to visualize.
    bands: Order of the bands.
    factor: Rescaling factor to
    grid: Show grid on visualization

    Returns None
    -------

    """
    def visualize_single_idx(axis, ts):
        axis.imshow(np.clip(eopatch.data[feature_name][ts][..., bands] * factor, 0, 1), extent=get_extent(eopatch))
        if grid:
            axis.grid()
            axis.set_title(f'{feature_name} {eopatch.timestamp[ts]}')

    if isinstance(time_idx, int):
        time_idx = [time_idx]
    if len(time_idx) == 1:
        visualize_single_idx(ax, time_idx[0])
    else:
        for i, tidx in enumerate(time_idx):
            visualize_single_idx(ax[i], tidx)

def unzip_file(gzfilename, filename, delete=False):
    """ Helper function to unzip files and optionally delete them after decompression
    """
    if not os.path.exists(filename):
        with gzip.open(gzfilename, 'rb') as f_in:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    if delete:
        os.remove(gzfilename)

def _parse_s3_timestamps(tiles, offset=2100):
    timestamps = []
    for tile in sorted(tiles):
        day, hour = tile.split('_SYN_')[-1].split('_')
        day = int(day)-offset
        timestamps.append(datetime.strptime(f'{day}{hour[:3]}', '%jT%H'))
    return timestamps
        
def _parse_s5p_timestamps(tiles, offset=2100):
    timestamps = []
    for tile in sorted(tiles):
        day, hour = tile.split('_day')[-1].split('_')
        day = int(day)-offset
        timestamps.append(datetime.strptime(f'{day}{hour[:3]}', '%jT%H'))
    return timestamps

def _parse_modis_timestamps(tiles):
    return [datetime.strptime(tile.split('.')[1], 'A%Y%j') 
                     for tile in sorted(tiles)]

def _parse_era5_timestamps(tiles, offset=2100):
    timestamps = []
    for tile in sorted(tiles):
        day, hour = tile.split('_day')[-1].split('_')
        day = int(day)-offset
        timestamps.append(datetime.strptime(f'{day}{hour[:3]}', '%jh%H'))
    return timestamps

TIMESTAMP_PARSER = dict(s5p=_parse_s5p_timestamps,
                        modis=_parse_modis_timestamps,
                        era5=_parse_era5_timestamps,
                        cams=_parse_era5_timestamps,
                        s3=_parse_s3_timestamps)

def load_tiffs(datapath, 
               feature, 
               filename=None,
               image_dtype=np.float32, 
               no_data_value=np.nan, 
               data_source='s5p', 
               offset=2100):
    """ Helper function to load the data sources provided as tiffs """
    assert data_source in ['s5p', 'modis', 'era5', 'cams', 's3']
    
    tiles = sorted(os.listdir(datapath)) if filename is None else [filename]

    # only keep files
    tiles = [tile for tile in tiles if not os.path.isdir(datapath/tile)]

    # unzip tiffs if they have .gz extension and delete them
    compressed_tiles = [tile for tile in tiles if tile.find('.gz') >= 0]
    for ctile in compressed_tiles:
        uctile = ctile.split('.gz')[0]
        unzip_file(str(datapath/ctile), str(datapath/uctile), delete=True)
    
    tiles = [tile if tile.find('.gz') < 0 else tile.split('.gz')[0]
             for tile in tiles]
    
    # remove files which don't have .tif extension
    tiles = [tile for tile in tiles if os.path.splitext(tile)[1] == '.tif']

    timestamp_size = len(tiles) if feature[0].is_time_dependent() else None
    
    import_task = ImportFromTiff(feature=feature, 
                                 folder=datapath,
                                 image_dtype=image_dtype,
                                 no_data_value=no_data_value,
                                 timestamp_size=len(tiles))
                                 
    if not feature[0].is_time_dependent():
        assert len(tiles) == 1
        return import_task.execute(filename=tiles[0])
    
    assert len(tiles) > 1
    eop = import_task.execute(filename=(sorted(tiles)))
    eop.timestamp = TIMESTAMP_PARSER[data_source](sorted(tiles), offset)

    return eop
