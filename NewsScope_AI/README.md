# 📰 NewsScope AI

NewsScope AI is a Python-based Natural Language Processing (NLP) project that analyzes news articles from a CSV dataset. It performs text preprocessing, keyword extraction, news classification, sentiment analysis, trend analysis, visualization, and report generation.

---

## 📌 Features

- Load news articles from CSV
- Text preprocessing using NLTK
- Tokenization
- Keyword extraction using TF-IDF
- News classification using Machine Learning
- Sentiment analysis using TextBlob
- Trend analysis
- Category-wise analysis
- Generate charts
- Generate Word Cloud
- Generate text report
- Save processed dataset

---

## 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TextBlob
- Matplotlib
- WordCloud

---

## 📂 Project Structure

```
NewsScope_AI/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── news.csv
│   ├── processed_news.csv
│   └── reports/
│       ├── news_analysis_report.txt
│       ├── category_chart.png
│       ├── sentiment_chart.png
│       ├── daily_trend.png
│       └── wordcloud.png
│
├── modules/
│   ├── loader.py
│   ├── preprocess.py
│   ├── tokenizer.py
│   ├── keywords.py
│   ├── classifier.py
│   ├── sentiment.py
│   ├── trends.py
│   ├── report.py
│   ├── visualization.py
│   └── logger.py
│
└── utils/
    └── helpers.py
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Download NLTK resources:

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Output

After execution, the following files will be generated:

```
processed_news.csv

news_analysis_report.txt

category_chart.png

sentiment_chart.png

daily_trend.png

wordcloud.png

news_scope.log
```

---

## 🧠 Modules

- Loader Module
- Preprocessing Module
- Tokenizer Module
- Keyword Extraction Module
- News Classifier Module
- Sentiment Analysis Module
- Trend Analysis Module
- Visualization Module
- Report Generator Module

---

## 🚀 Future Enhancements

- Real-time news collection using News APIs
- Web-based dashboard using Flask
- Streamlit interface
- Deep Learning-based classification
- Multi-language support
- PDF report generation
- Email report automation

---

## 👨‍💻 Author

Developed as a Python NLP Project using Machine Learning and Data Analysis techniques.