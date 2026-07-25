"""
keywords.py
-------------------------
Keyword extraction using TF-IDF.
"""

from sklearn.feature_extraction.text import TfidfVectorizer

from config import MAX_KEYWORDS
from modules.logger import logger


class KeywordExtractor:

    def __init__(self, max_keywords=MAX_KEYWORDS):
        self.max_keywords = max_keywords

    def extract_keywords(self, text):
        """
        Extract keywords from a single article.
        """

        try:
            if not isinstance(text, str) or text.strip() == "":
                return []

            vectorizer = TfidfVectorizer(
                stop_words="english",
                max_features=self.max_keywords
            )

            vectorizer.fit([text])

            return list(vectorizer.get_feature_names_out())

        except Exception as e:
            logger.error(f"Keyword extraction failed: {e}")
            return []

    def process_dataframe(self, dataframe):
        """
        Add keywords column.
        """

        if "clean_content" not in dataframe.columns:
            logger.error("clean_content column not found.")
            return dataframe

        dataframe["keywords"] = dataframe["clean_content"].apply(
            self.extract_keywords
        )

        logger.info("Keyword extraction completed.")

        return dataframe

    def get_all_keywords(self, dataframe):

        if "keywords" not in dataframe.columns:
            return []

        keywords = []

        for item in dataframe["keywords"]:
            keywords.extend(item)

        return keywords

    def keyword_frequency(self, dataframe):

        frequency = {}

        for word in self.get_all_keywords(dataframe):
            frequency[word] = frequency.get(word, 0) + 1

        return dict(
            sorted(
                frequency.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )

    def top_keywords(self, dataframe, top_n=10):

        return list(self.keyword_frequency(dataframe).items())[:top_n]