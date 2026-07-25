"""
logger.py
------------------
Logging module for NewsScope AI
"""

import logging
import os
from config import LOG_FILE


def setup_logger():
    """
    Creates and configures the project logger.
    """

    # Create log folder if it doesn't exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logger = logging.getLogger("NewsScopeAI")

    # Prevent duplicate log entries
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Save logs to file
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Display logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Create a global logger object
logger = setup_logger()