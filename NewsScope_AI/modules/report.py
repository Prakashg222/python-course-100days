"""
report.py
-------------------------
Generate analysis reports for NewsScope AI
"""

import os
from datetime import datetime

from config import REPORT_FOLDER, REPORT_NAME
from modules.logger import logger


class ReportGenerator:
    """
    Generate and save a text report of the analysis.
    """

    def __init__(self):
        self.report_path = os.path.join(REPORT_FOLDER, REPORT_NAME)

    def generate_report(self, dataframe, trend_summary, avg_polarity):
        """
        Create a text report and save it.
        """

        total_articles = len(dataframe)

        with open(self.report_path, "w", encoding="utf-8") as report:

            report.write("=" * 60 + "\n")
            report.write("              NEWSSCOPE AI REPORT\n")
            report.write("=" * 60 + "\n\n")

            report.write(
                f"Generated On : {datetime.now()}\n"
            )

            report.write(
                f"Total News Articles : {total_articles}\n\n"
            )

            # Category Summary
            report.write("-" * 50 + "\n")
            report.write("CATEGORY SUMMARY\n")
            report.write("-" * 50 + "\n")

            for category, count in trend_summary["Categories"].items():
                report.write(f"{category:<20} : {count}\n")

            report.write("\n")

            # Sentiment Summary
            report.write("-" * 50 + "\n")
            report.write("SENTIMENT SUMMARY\n")
            report.write("-" * 50 + "\n")

            for sentiment, count in trend_summary["Sentiments"].items():
                report.write(f"{sentiment:<20} : {count}\n")

            report.write(
                f"\nAverage Polarity : {avg_polarity}\n\n"
            )

            # Top Keywords
            report.write("-" * 50 + "\n")
            report.write("TOP KEYWORDS\n")
            report.write("-" * 50 + "\n")

            for keyword, count in trend_summary["Top Keywords"]:
                report.write(f"{keyword:<20} : {count}\n")

            report.write("\n")

            # Daily Trends
            report.write("-" * 50 + "\n")
            report.write("DAILY NEWS TREND\n")
            report.write("-" * 50 + "\n")

            for day, count in trend_summary["Daily News"].items():
                report.write(f"{day:<20} : {count}\n")

            report.write("\n")
            report.write("=" * 60 + "\n")
            report.write("End of Report\n")
            report.write("=" * 60 + "\n")

        logger.info("Report generated successfully.")

        return self.report_path