"""
trends.py
-------------------------
Trend Analysis Module for NewsScope AI
"""

from collections import Counter
from modules.logger import logger


class TrendAnalyzer:
    """
    Analyze trending keywords and categories.
    """

    def keyword_trends(self, dataframe, top_n=10):
        """
        Return the most frequent keywords.
        """

        if "keywords" not in dataframe.columns:
            logger.error("keywords column not found.")
            return []

        all_keywords = []

        for keyword_list in dataframe["keywords"]:
            if isinstance(keyword_list, list):
                all_keywords.extend(keyword_list)

        counter = Counter(all_keywords)

        logger.info("Keyword trends generated.")

        return counter.most_common(top_n)

    def category_trends(self, dataframe):
        """
        Count articles in each category.
        """

        if "category" not in dataframe.columns:
            logger.error("category column not found.")
            return {}

        trends = dataframe["category"].value_counts().to_dict()

        logger.info("Category trends generated.")

        return trends

    def sentiment_trends(self, dataframe):
        """
        Count Positive, Negative and Neutral news.
        """

        if "sentiment" not in dataframe.columns:
            logger.error("sentiment column not found.")
            return {}

        trends = dataframe["sentiment"].value_counts().to_dict()

        logger.info("Sentiment trends generated.")

        return trends

    def daily_news_trend(self, dataframe):
        """
        Count news articles by date.
        """

        if "date" not in dataframe.columns:
            logger.error("date column not found.")
            return {}

        trends = dataframe["date"].value_counts().sort_index().to_dict()

        logger.info("Daily news trends generated.")

        return trends

    def overall_summary(self, dataframe):
        """
        Generate complete trend summary.
        """

        summary = {
            "Top Keywords": self.keyword_trends(dataframe),
            "Categories": self.category_trends(dataframe),
            "Sentiments": self.sentiment_trends(dataframe),
            "Daily News": self.daily_news_trend(dataframe)
        }

        logger.info("Overall trend summary created.")

        return summary