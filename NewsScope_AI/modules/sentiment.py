"""
sentiment.py
-------------------------
Sentiment Analysis Module for NewsScope AI
"""

from textblob import TextBlob
from modules.logger import logger


class SentimentAnalyzer:
    """
    Analyze sentiment of news articles.
    """

    def analyze_sentiment(self, text):
        """
        Returns sentiment label and polarity score.
        """

        if not isinstance(text, str) or text.strip() == "":
            return ("Neutral", 0.0)

        analysis = TextBlob(text)

        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return (sentiment, round(polarity, 2))

    def analyze_dataframe(self, dataframe):
        """
        Analyze sentiment for each news article.
        """

        if "clean_content" not in dataframe.columns:
            logger.error("clean_content column not found.")
            return dataframe

        sentiments = dataframe["clean_content"].apply(
            self.analyze_sentiment
        )

        dataframe["sentiment"] = sentiments.apply(lambda x: x[0])
        dataframe["polarity"] = sentiments.apply(lambda x: x[1])

        logger.info("Sentiment analysis completed.")

        return dataframe

    def sentiment_summary(self, dataframe):
        """
        Count Positive, Negative and Neutral news.
        """

        if "sentiment" not in dataframe.columns:
            logger.error("Sentiment column not found.")
            return {}

        summary = dataframe["sentiment"].value_counts().to_dict()

        return summary

    def average_polarity(self, dataframe):
        """
        Calculate average polarity score.
        """

        if "polarity" not in dataframe.columns:
            return 0.0

        return round(dataframe["polarity"].mean(), 2)