"""
tokenizer.py
-------------------------
Tokenization module for NewsScope AI
"""

import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

from modules.logger import logger

# Download tokenizer data (only first time)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


class NewsTokenizer:
    """
    Tokenizes cleaned news text and counts word frequencies.
    """

    def tokenize_text(self, text):
        """
        Convert text into a list of tokens.
        """

        if not isinstance(text, str):
            return []

        tokens = word_tokenize(text)

        # Keep only alphabetic words
        tokens = [
            word.lower()
            for word in tokens
            if word.isalpha()
        ]

        logger.info("Text tokenized successfully.")

        return tokens

    def tokenize_dataframe(self, dataframe):
        """
        Tokenize the clean_content column.
        """

        if "clean_content" not in dataframe.columns:
            logger.error("clean_content column not found.")
            return dataframe

        dataframe["tokens"] = dataframe["clean_content"].apply(
            self.tokenize_text
        )

        logger.info("DataFrame tokenization completed.")

        return dataframe

    def word_frequency(self, dataframe):
        """
        Count word frequencies from all tokenized news.
        """

        if "tokens" not in dataframe.columns:
            logger.error("tokens column not found.")
            return {}

        all_words = []

        for token_list in dataframe["tokens"]:
            all_words.extend(token_list)

        frequency = Counter(all_words)

        logger.info("Word frequency calculated.")

        return frequency

    def top_words(self, dataframe, top_n=10):
        """
        Return the most common words.
        """

        frequency = self.word_frequency(dataframe)

        return frequency.most_common(top_n)