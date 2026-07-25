"""
classifier.py
-------------------------
News classification module using Machine Learning.
"""

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from modules.logger import logger


class NewsClassifier:
    """
    Classifies news into categories.
    """

    def __init__(self):
        self.model = Pipeline([
            ("tfidf", TfidfVectorizer(stop_words="english")),
            ("classifier", MultinomialNB())
        ])
        self.is_trained = False

    def train(self, dataframe):

        required_columns = ["clean_content", "category"]

        for column in required_columns:
            if column not in dataframe.columns:
                logger.error(f"Missing column: {column}")
                return dataframe

        X = dataframe["clean_content"]
        y = dataframe["category"]

        self.model.fit(X, y)

        self.is_trained = True

        logger.info("News classification model trained successfully.")

        return dataframe

    def predict(self, text):
        """
        Predict category for a single news article.
        """

        if not self.is_trained:
            logger.error("Model is not trained.")
            return "Unknown"

        prediction = self.model.predict([text])[0]

        return prediction

    def classify_dataframe(self, dataframe):
        """
        Predict category for every news article.
        """

        if not self.is_trained:
            logger.error("Train the model first.")
            return dataframe

        dataframe["predicted_category"] = dataframe[
            "clean_content"
        ].apply(self.predict)

        logger.info("News classification completed.")

        return dataframe

    def accuracy(self, dataframe):
        """
        Calculate training accuracy.
        """

        if not self.is_trained:
            return 0

        X = dataframe["clean_content"]
        y = dataframe["category"]

        accuracy = self.model.score(X, y)

        return round(accuracy * 100, 2)