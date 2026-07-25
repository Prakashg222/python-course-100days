"""
config.py
------------
Project configuration settings for NewsScope AI
"""

import os

# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
REPORT_FOLDER = os.path.join(DATA_FOLDER, "reports")

NEWS_CSV = os.path.join(DATA_FOLDER, "news.csv")
NEWS_JSON = os.path.join(DATA_FOLDER, "news.json")

LOG_FILE = os.path.join(BASE_DIR, "news_scope.log")

# ==============================
# News Categories
# ==============================

CATEGORIES = [
    "Politics",
    "Sports",
    "Technology",
    "Business",
    "Entertainment",
    "Health",
    "Education",
    "Science"
]

# ==============================
# NLP Settings
# ==============================

MAX_KEYWORDS = 10

STOPWORDS_LANGUAGE = "english"

MIN_WORD_LENGTH = 3

# ==============================
# Sentiment Labels
# ==============================

POSITIVE = "Positive"
NEGATIVE = "Negative"
NEUTRAL = "Neutral"

# ==============================
# Visualization Settings
# ==============================

FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6

BAR_COLOR = "steelblue"

# ==============================
# Report Settings
# ==============================

REPORT_NAME = "news_analysis_report.txt"

# ==============================
# Create Required Folders
# ==============================

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)