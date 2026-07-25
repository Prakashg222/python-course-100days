"""
main.py
------------------------------------
NewsScope AI - Main Application
"""

from modules.loader import NewsLoader
from modules.preprocess import TextPreprocessor
from modules.tokenizer import NewsTokenizer
from modules.keywords import KeywordExtractor
from modules.classifier import NewsClassifier
from modules.sentiment import SentimentAnalyzer
from modules.trends import TrendAnalyzer
from modules.report import ReportGenerator
from modules.visualization import Visualizer

from utils.helpers import (
    validate_dataframe,
    dataset_info,
    preview_data,
    save_dataframe
)


def main():

    print("=" * 60)
    print("        Welcome to NewsScope AI")
    print("=" * 60)

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    loader = NewsLoader()

    df = loader.load_csv()

    if not validate_dataframe(df):
        print("Dataset loading failed.")
        return

    dataset_info(df)

    preview_data(df)

    # --------------------------------------------------
    # Text Preprocessing
    # --------------------------------------------------

    print("\nPreprocessing text...")

    processor = TextPreprocessor()

    df = processor.preprocess_dataframe(df)

    # --------------------------------------------------
    # Tokenization
    # --------------------------------------------------

    print("Tokenizing news...")

    tokenizer = NewsTokenizer()

    df = tokenizer.tokenize_dataframe(df)

    print("\nTop 10 Frequent Words")

    print(tokenizer.top_words(df))

    # --------------------------------------------------
    # Keyword Extraction
    # --------------------------------------------------

    print("\nExtracting keywords...")

    keyword = KeywordExtractor()

    df = keyword.process_dataframe(df)

    print("\nTop Keywords")

    print(keyword.top_keywords(df))

    # --------------------------------------------------
    # Classification
    # --------------------------------------------------

    print("\nTraining News Classifier...")

    classifier = NewsClassifier()

    classifier.train(df)

    accuracy = classifier.accuracy(df)

    print(f"\nTraining Accuracy : {accuracy}%")

    df = classifier.classify_dataframe(df)

    # --------------------------------------------------
    # Sentiment Analysis
    # --------------------------------------------------

    print("\nAnalyzing Sentiment...")

    sentiment = SentimentAnalyzer()

    df = sentiment.analyze_dataframe(df)

    summary = sentiment.sentiment_summary(df)

    average = sentiment.average_polarity(df)

    print("\nSentiment Summary")

    print(summary)

    print(f"\nAverage Polarity : {average}")

    # --------------------------------------------------
    # Trend Analysis
    # --------------------------------------------------

    print("\nAnalyzing Trends...")

    trend = TrendAnalyzer()

    trend_summary = trend.overall_summary(df)

    print("\nCategory Distribution")

    print(trend_summary["Categories"])

    # --------------------------------------------------
    # Generate Charts
    # --------------------------------------------------

    print("\nGenerating Charts...")

    visual = Visualizer()

    visual.category_chart(
        trend_summary["Categories"]
    )

    visual.sentiment_chart(
        trend_summary["Sentiments"]
    )

    visual.daily_trend_chart(
        trend_summary["Daily News"]
    )

    keywords = [
        word
        for word, count in trend_summary["Top Keywords"]
    ]

    visual.keyword_wordcloud(keywords)

    # --------------------------------------------------
    # Generate Report
    # --------------------------------------------------

    print("\nGenerating Report...")

    report = ReportGenerator()

    report_path = report.generate_report(
        dataframe=df,
        trend_summary=trend_summary,
        avg_polarity=average
    )

    print(f"\nReport Saved At:\n{report_path}")

    # --------------------------------------------------
    # Save Processed Dataset
    # --------------------------------------------------

    save_dataframe(
        df,
        "data/processed_news.csv"
    )

    print("\nProcessed dataset saved.")

    print("\nProject Completed Successfully!")

    print("=" * 60)


if __name__ == "__main__":
    main()