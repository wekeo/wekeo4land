# Exploring the CLMS HR-S&I dataset using Datacubes

---

In this demonstration Jupyter Notebook, we will be requesting and visualising CLMS HR-S&I data with xcube and other datacube technologies in the EDC EOxHub Workplace.

## Intro to datacubes

Datacubes are powerful datastructures which provide easy access to large amounts of data. Raw datacubes provide this data indiscriminately to the user, that means that all data is available, no matter the quality of the data.

As an example, Sentinel 2 data is available in the form of single tiles, without any cloud masking applied. This has the advantage that no decisions about the data is made by the data provider, leaving the full set of possibilities to work with the data open to the user.However this also makes it the users responsibility to coerce the data into formats which are usable for analysis. For example by masking out clouds or mosaicking the data.The two main ways that datacubes are handled are:

- Spatial aggregation
- Temporal aggregation

These two high level concepts allow you to go from terabytes of data to kilobytes of analysis ready data. In this use case we will look at how those aggregations can be performed on a data cube. In a last step we will also see how these approaches can be scaled up to continental scale.

# Overview notebooks

The notebooks are split like this:

- Notebook 00: Exploration of the data using xcube
- Notebook 01: Analysing persistent snow cover, simple intro to datacubes
- Notebook 02: Analysing fractional snow cover, showing on the fly temporal aggregation
- Notebook 03: Analysing snow state, also showing on the fly temporal aggregation using different data
- Notebook 04: Scaling up the workflow to larger spatial areas using batch processing  

# How to run the Notebooks in Euro Data Cube
The Notebooks can be run in [Euro Data Cube](https://eurodatacube.com/). An EDC account, EOxHub Workspace and EDC Sentinel Hub subscription is needed. (Free trial subscriptions are available)
- Register for EDC account [here](https://eurodatacube.com/register) and activate the EOxHub Workspace.
- Activate a free trial subscription of [EDC Sentinel Hub](https://eurodatacube.com/marketplace/services/edc_sentinel_hub).
- Proceed to upload the Notebooks to EDC Jupyter Hub. 

