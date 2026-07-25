"""
loader.py
-------------------------
Loads news data from CSV or JSON files.
"""

import os
import json
import pandas as pd

from config import NEWS_CSV, NEWS_JSON
from modules.logger import logger


class NewsLoader:
    """
    Load news data from CSV or JSON.
    """

    REQUIRED_COLUMNS = ["title", "category", "date", "content"]

    def load_csv(self, file_path=NEWS_CSV):
        """
        Load news from CSV file.
        """

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"{file_path} does not exist.")

            df = pd.read_csv(file_path)

            self.validate_columns(df)

            logger.info("CSV file loaded successfully.")

            return df

        except Exception as e:
            logger.error(f"Error loading CSV: {e}")
            return pd.DataFrame()

    def load_json(self, file_path=NEWS_JSON):
        """
        Load news from JSON file.
        """

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"{file_path} does not exist.")

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            df = pd.DataFrame(data)

            self.validate_columns(df)

            logger.info("JSON file loaded successfully.")

            return df

        except Exception as e:
            logger.error(f"Error loading JSON: {e}")
            return pd.DataFrame()

    def validate_columns(self, dataframe):
        """
        Validate required columns.
        """

        missing = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {', '.join(missing)}"
            )

        logger.info("Dataset validation successful.")