
# ETC-DI-AI Workshop

## Overview

This repository contains three Jupyter Notebooks that are designed to work in the Wekeo Jupyter Hub environment. The notebooks cover different aspects of data preparation, model selection, and scaling up with EO-Learn. The instructions provided here will help you set up the necessary environment and run the notebooks successfully.

## Notebooks

The following notebooks are available in this repository:

1. Data Preparation: This notebook provides step-by-step instructions for preparing data for supervised machine learning.

2. Model Selection: This notebook focuses on cleaning and preprocessing satellite data for a machine learning task. It includes guidelines for training, evaluating, and selecting a model for a large-scale application using the cleaned data.

3. Scaling Up with EO-Learn 3: This notebook demonstrates how to scale up the previous analysis to the country level. It discusses the challenges involved in handling large amounts of data and utilizes the `eo-learn` library to address these challenges.

## Folders

The repository includes the following folders:

1. data: Contains the raw data used in the notebooks.

2. images: Contains auxiliary images used in the notebooks.

## Files

- environment.yml: This file provides the necessary dependencies for setting up the Conda environment required to run the notebooks.

## To run notebooks in WEKEO

To run the notebooks in this repository, please follow these installation instructions:

1. Clone the repository by opening the terminal and executing the following command:

   ```
   git clone https://github.com/eea/clms-data-science-applications.git
   cd clms-data-science-applications
   ```

2. Create a Conda environment from the provided YAML file:

   ```
   conda env create -f environment.yml
   ```

3. Activate the environment:

   ```
   conda activate environment_name
   ```

4. Install the ipykernel package:

   ```
   conda install ipykernel
   ```

5. Register the Conda environment as a kernel:

   ```
   python -m ipykernel install --user --name=environment_name
   ```

6. Restart the kernels to see the newly registered kernel.

7. Create a file named `credentials.py` in the root of the folder and input your credentials for SH and Wekeo:

   ```python
   CLIENT_ID = '*******'
   CLIENT_SECRET = '*******'
   WEKEO_USER = '*******'
   WEKEO_PASSWORD = '*******'
   ```

Please make sure to replace the asterisks (`*******`) with your actual credentials.

8. Download the Ground Truth data (Eurocrops Netherlands) from [here](https://zenodo.org/record/7476474/files/NL_2020.zip?download=1) and unzip it into ./data
