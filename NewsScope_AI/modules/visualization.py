"""
visualization.py
-------------------------
Visualization Module for NewsScope AI
"""

import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from config import REPORT_FOLDER
from modules.logger import logger


class Visualizer:
    """
    Generate charts and word clouds.
    """

    def __init__(self):
        self.output_folder = REPORT_FOLDER

    def category_chart(self, category_data):
        """
        Generate a bar chart for news categories.
        """

        plt.figure(figsize=(10, 6))

        plt.bar(category_data.keys(), category_data.values())

        plt.title("News Category Distribution")
        plt.xlabel("Category")
        plt.ylabel("Number of Articles")

        plt.xticks(rotation=30)

        path = os.path.join(
            self.output_folder,
            "category_chart.png"
        )

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        logger.info("Category chart generated.")

    def sentiment_chart(self, sentiment_data):
        """
        Generate a pie chart for sentiment analysis.
        """

        plt.figure(figsize=(6, 6))

        plt.pie(
            sentiment_data.values(),
            labels=sentiment_data.keys(),
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Sentiment Distribution")

        path = os.path.join(
            self.output_folder,
            "sentiment_chart.png"
        )

        plt.savefig(path)
        plt.close()

        logger.info("Sentiment chart generated.")

    def daily_trend_chart(self, daily_data):
        """
        Generate a line chart for daily news trends.
        """

        plt.figure(figsize=(10, 6))

        plt.plot(
            list(daily_data.keys()),
            list(daily_data.values()),
            marker="o"
        )

        plt.title("Daily News Trend")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")

        plt.xticks(rotation=45)

        path = os.path.join(
            self.output_folder,
            "daily_trend.png"
        )

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        logger.info("Daily trend chart generated.")

    def keyword_wordcloud(self, keywords):
        """
        Generate a word cloud from keywords.
        """

        text = " ".join(keywords)

        cloud = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(text)

        plt.figure(figsize=(12, 6))
        plt.imshow(cloud)
        plt.axis("off")

        path = os.path.join(self.output_folder, "wordcloud.png")

        plt.savefig(path)
        plt.show()
        plt.close()

        logger.info("Word cloud generated.")