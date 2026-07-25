"""
preprocess.py
-------------------------
Text preprocessing module for NewsScope AI
"""

import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from modules.logger import logger

# Download required NLTK resources (only first time)
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

# Initialize
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


class TextPreprocessor:
    """
    Cleans and preprocesses news text.
    """

    def clean_text(self, text):
        """
        Perform text preprocessing.
        """

        if not isinstance(text, str):
            return ""

        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove email addresses
        text = re.sub(r"\S+@\S+", "", text)

        # Remove numbers
        text = re.sub(r"\d+", "", text)

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Remove stopwords and lemmatize
        words = []

        for word in text.split():

            if word not in stop_words and len(word) > 2:
                word = lemmatizer.lemmatize(word)
                words.append(word)

        cleaned_text = " ".join(words)

        logger.info("Text preprocessing completed.")

        return cleaned_text

    def preprocess_dataframe(self, dataframe):
        """
        Apply preprocessing to the 'content' column.
        """

        if "content" not in dataframe.columns:
            logger.error("Content column not found.")
            return dataframe

        dataframe["clean_content"] = dataframe["content"].apply(
            self.clean_text
        )

        logger.info("DataFrame preprocessing completed.")

        return dataframe