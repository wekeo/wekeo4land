# Welcome to WEkEO4Land

**wekeo4land** is a repository of Python based tools to introduce you to the use of land related data on the [WEkEO DIAS (Data Information
and Access System)](https://wekeo.eu/) and its Jupyter Lab. The content includes notebooks explaining WEkEO and the Jupyter Lab environment and
how to use the Harmonised Data Access (HDA) API that is fundamental to WEkEO. Within this repository are 
tutorials and case studies, using data from the Copernicus Programme that are available on WEkEO and written by expert trainers
from Mercator Ocean International, ECMWF and EUMETSAT.

The content provided is mostly based on [Jupyter Notebooks](https://jupyter.org/), which allow
a high-level of interactive learning, as code, text description and visualisation 
is combined in one place. 

## Copernicus Data
The notebooks contained within the repository feature data from the Sentinel-2 satellite
# Welcome to WEkEO4Land

**wekeo4land** is a repository of Python based tools to introduce you to the use of land related data on the [WEkEO DIAS (Data Information
and Access System)](https://wekeo.eu/) and its Jupyter Lab. The content includes notebooks explaining WEkEO and the Jupyter Lab environment and
how to use the Harmonised Data Access (HDA) API that is fundamental to WEkEO. Within this repository are 
tutorials and case studies, using data from the Copernicus Programme that are available on WEkEO and written by expert trainers.

The content provided is mostly based on [Jupyter Notebooks](https://jupyter.org/), which allow
a high-level of interactive learning, as code, text description and visualisation 
is combined in one place. 

## Copernicus Data
The notebooks contained within the repository feature data from the Sentinel-2 satellite

## Repository overview
This repository is organized in to 2 case studies on (i) land and (ii) snow&ice.For each case study a set of Copernicus data is introduced that is suitable for land or snow&ice applications and available via WEkEO. Each dataset is introduced via two notebooks: the first notebooks show how to retrieve the respective dataset from WEkEO (retrieve notebooks) and the second notebook offers a practical example on how to load, browse and visualise the dataset (explore notebooks). The following notebook are available:
* Case study **land** (folder `./land/`):
  * [Downlaod and processing Sentinal-2 Scene and CLMS CORINE Land Cover(CLC) data](./land/Land_S2_CLC_donalod.ipynb)
  In this case study we will use the WEkEO Jupyterhub to access and analyse data from the Copernicus Sentinel-2 and products from the Copernicus Land Monitoring Service (CLMS). A region in northern Corsica has been selected as it contains representative landscape features and process elements which can be used to demonstrate the capabilities and strengths of Copernicus space component and services

<br>

* Case study **snow&ice** (folder `./snow&ice/`):
   * [Accessing , reading and visualzing Gap Filled Fractional Snow Cover (GFSC) product](./snow&ice/clms_hrsi_gfsc_demo.ipynb)
   In this case study we will access, read and visualize GFSC products through HDA API. Manipulate 
   * [Analyse wet snow extent](./snow&ice/getWSMElevStats-template.ipynb)
   Analyse wet snow extent from SWS time series in dependence of altitude
   * [Analyse wet snow extent in dependence of altituds and local aspect](./snow&ice/getWSMaspectStats-template.ipynb)
   Analyse wet snow extent from SWS time series in dependence of altitude and local aspect


## How to use this material

If you are on GitHub/Lab you can visit www.wekeo.eu, register for an account and enter the JupyterLab - then follow the instructions below. 

If you are currently on the WEkEO JupyterLab you're already in the right place and can start. To clone this repository in to the WEkEO JupyterLab environment open a terminal in the WEkEO JupyterLab, type 
  > `cd work`<br>
  > `git clone --recurse-submodules https://github.com/wekeo/wekeo4land.git`<br> 
 
 This will create a clone of this repository of notebooks in the work directory on your Jupyterlab instance. You can use the same shell script to clone any external repository you like.

You can also use this code on your own computer/Jupyter Lab server, however you won't have the fast access provided by the Harmonized Data Access as part of the WEkEO infrastructure.


### Recommended python set up

This repository supports Python 3.7. We highly recommend that users working on their own systems install the appropriate Anaconda distribution for their operating system. Here is a link to the [Anaconda distribution of Python 3.7](https://www.anaconda.com/products/individual).

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - by which we refer to those no included by default in Anaconda. These are included in the JupyterLab environment but you may need to install them for local working.

## Where to find what you need
The content of this repository is suitable for those completely new to WEkEO, Python, Copernicus data
and hosted processing environments.

Below is a summary of the files provided, with recommendations on where to start:

FILL IN


## How to use this material

If you are on GitHub/Lab you can visit www.wekeo.eu, register for an account and enter the JupyterLab - then follow the instructions below. 

If you are currently on the WEkEO JupyterLab you're already in the right place and can start. To clone this repository in to the WEkEO JupyterLab environment open a terminal in the WEkEO JupyterLab, type 
  > `cd work`<br>
  > `git clone https://github.com/wekeo/wekeo4land.git`<br> 
 
 This will create a clone of this repository of notebooks in the work directory on your Jupyterlab instance. You can use the same shell script to clone any external repository you like.

You can also use this code on your own computer/Jupyter Lab server, however you won't have the fast access provided by the Harmonized Data Access as part of the WEkEO infrastructure.


### Recommended python set up

This repository supports Python 3.7. We highly recommend that users working on their own systems install the appropriate Anaconda distribution for their operating system. Here is a link to the [Anaconda distribution of Python 3.7](https://www.anaconda.com/products/individual).

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - by which we refer to those no included by default in Anaconda. These are included in the JupyterLab environment but you may need to install them for local working.




