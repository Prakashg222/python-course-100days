"""
helpers.py
-------------------------
Utility functions for NewsScope AI
"""

import os
import pandas as pd

from modules.logger import logger


def validate_dataframe(dataframe):
    """
    Check whether the DataFrame is valid.
    """

    if dataframe is None:
        logger.error("DataFrame is None.")
        return False

    if dataframe.empty:
        logger.error("DataFrame is empty.")
        return False

    return True


def save_dataframe(dataframe, output_path):
    """
    Save DataFrame to CSV.
    """

    try:
        dataframe.to_csv(output_path, index=False)
        logger.info(f"Data saved to {output_path}")

    except Exception as e:
        logger.error(f"Unable to save DataFrame: {e}")


def print_heading(title):
    """
    Print a formatted heading.
    """

    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def print_dictionary(dictionary):
    """
    Print dictionary in a readable format.
    """

    for key, value in dictionary.items():
        print(f"{key:<25} : {value}")


def print_list(items):
    """
    Print list items.
    """

    for item in items:
        print(item)


def create_folder(folder_path):
    """
    Create folder if it does not exist.
    """

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f"Folder created: {folder_path}")


def dataset_info(dataframe):
    """
    Display dataset information.
    """

    print_heading("DATASET INFORMATION")

    print(f"Rows    : {dataframe.shape[0]}")
    print(f"Columns : {dataframe.shape[1]}")

    print("\nColumn Names:")

    for column in dataframe.columns:
        print(f" - {column}")


def missing_values(dataframe):
    """
    Display missing values.
    """

    print_heading("MISSING VALUES")

    print(dataframe.isnull().sum())


def preview_data(dataframe, rows=5):
    """
    Display first few rows.
    """

    print_heading("DATA PREVIEW")

    print(dataframe.head(rows))