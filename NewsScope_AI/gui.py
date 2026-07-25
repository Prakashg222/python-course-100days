import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from modules.loader import NewsLoader
from modules.preprocess import TextPreprocessor
from modules.tokenizer import NewsTokenizer
from modules.keywords import KeywordExtractor
from modules.classifier import NewsClassifier
from modules.sentiment import SentimentAnalyzer
from modules.visualization import Visualizer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

df = None

# ---------------- Functions ---------------- #

def load_dataset():
    global df

    try:
        loader = NewsLoader()
        df = loader.load_csv()

        status_label.configure(
            text=f"Dataset Loaded : {len(df)} Articles",
            text_color="#8EB69B"
        )

        articles_card.configure(text=str(len(df)))

        messagebox.showinfo(
            "Success",
            "Dataset Loaded Successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def analyze_news():
    global df

    if df is None:
        messagebox.showerror(
            "Error",
            "Load Dataset First"
        )
        return

    preprocess = TextPreprocessor()
    tokenizer = NewsTokenizer()
    keyword = KeywordExtractor()
    classifier = NewsClassifier()
    sentiment = SentimentAnalyzer()

    df = preprocess.preprocess_dataframe(df)
    df = tokenizer.tokenize_dataframe(df)
    df = keyword.process_dataframe(df)

    classifier.train(df)
    df = classifier.classify_dataframe(df)

    df = sentiment.analyze_dataframe(df)

    accuracy = classifier.accuracy(df)
    summary = sentiment.sentiment_summary(df)

    accuracy_card.configure(
    text=f"{accuracy}%"
)

    positive_card.configure(
    text=str(summary.get("Positive", 0))
)

    category_card.configure(
    text=str(df["category"].nunique())
)

    status_label.configure(
        text="Analysis Completed",
        text_color="#8EB69B"
    )

    messagebox.showinfo(
        "Success",
        "News Analysis Completed Successfully!"
    )


def generate_report():

    messagebox.showinfo(
        "Report",
        "Report Generated Successfully!"
    )


def show_charts():

    global df

    if df is None:
        messagebox.showerror(
            "Error",
            "Analyze dataset first"
        )
        return

    visualizer = Visualizer()

    category = df["category"].value_counts().to_dict()
    visualizer.category_chart(category)

    sentiment = SentimentAnalyzer()
    sentiment_data = sentiment.sentiment_summary(df)
    visualizer.sentiment_chart(sentiment_data)

    keywords = []

    for text in df["clean_content"]:
        keywords.extend(text.split())

    visualizer.keyword_wordcloud(keywords)

    messagebox.showinfo(
        "Charts",
        "Charts Generated Successfully!"
    )


# ---------------- Main Window ---------------- #

root = ctk.CTk()

root.title("NewsScope AI")

root.geometry("1300x750")

root.configure(fg_color="#051F20")

# ---------------- Sidebar ---------------- #

sidebar = ctk.CTkFrame(
    root,
    width=240,
    corner_radius=0,
    fg_color="#0B2B26"
)

sidebar.pack(
    side="left",
    fill="y"
)

logo = ctk.CTkLabel(
    sidebar,
    text="📰 NewsScope AI",
    font=("Segoe UI",26,"bold")
)

logo.pack(
    pady=(30,20)
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="🏠 Dashboard",
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

dashboard_btn.pack(pady=10)

load_btn = ctk.CTkButton(
    sidebar,
    text="📂 Load Dataset",
    command=load_dataset,
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

load_btn.pack(pady=10)

analyze_btn = ctk.CTkButton(
    sidebar,
    text="🤖 Analyze News",
    command=analyze_news,
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

analyze_btn.pack(pady=10)

report_btn = ctk.CTkButton(
    sidebar,
    text="📄 Generate Report",
    command=generate_report,
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

report_btn.pack(pady=10)

chart_btn = ctk.CTkButton(
    sidebar,
    text="📊 Charts",
    command=show_charts,
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

chart_btn.pack(pady=10)

setting_btn = ctk.CTkButton(
    sidebar,
    text="⚙ Settings",
    width=200,
    height=45,
    fg_color="#163832",
    hover_color="#235347",
    corner_radius=18
)

setting_btn.pack(pady=10)

exit_btn = ctk.CTkButton(
    sidebar,
    text="❌ Exit",
    command=root.destroy,
    width=200,
    height=45,
    fg_color="#7F1D1D",
    hover_color="#991B1B",
    corner_radius=18
)

exit_btn.pack(
    side="bottom",
    pady=30
)

# ---------------- Dashboard ---------------- #

main = ctk.CTkFrame(
    root,
    fg_color="#051F20"
)

main.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

title = ctk.CTkLabel(
    main,
    text="Dashboard",
    font=("Segoe UI",30,"bold")
)

title.pack(anchor="nw")
# ==========================
# Dashboard Cards
# ==========================

cards = ctk.CTkFrame(main, fg_color="transparent")
cards.pack(fill="x", pady=25)

def create_card(parent, title, value):

    card = ctk.CTkFrame(
        parent,
        width=180,
        height=120,
        corner_radius=20,
        fg_color="#163832"
    )

    card.pack(side="left", padx=15)
    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text=title,
        font=("Segoe UI", 16, "bold")
    ).pack(pady=(18,5))

    value_lbl = ctk.CTkLabel(
        card,
        text=value,
        font=("Segoe UI",30,"bold"),
        text_color="#8EB69B"
    )
    value_lbl.pack()

    return value_lbl


articles_card = create_card(cards, "📰 Articles", "0")
category_card = create_card(cards, "📂 Categories", "0")
accuracy_card = create_card(cards, "🤖 Accuracy", "0%")
positive_card = create_card(cards, "😊 Positive", "0")


# ==========================
# Bottom Buttons
# ==========================

buttons = ctk.CTkFrame(main, fg_color="transparent")
buttons.pack(pady=30)

analyze_btn = ctk.CTkButton(
    buttons,
    text="Analyze News",
    width=180,
    height=45,
    corner_radius=20,
    fg_color="#235347",
    hover_color="#163832",
    command=analyze_news
)
analyze_btn.grid(row=0,column=0,padx=15)

report_btn = ctk.CTkButton(
    buttons,
    text="Generate Report",
    width=180,
    height=45,
    corner_radius=20,
    fg_color="#235347",
    hover_color="#163832",
    command=generate_report
)
report_btn.grid(row=0,column=1,padx=15)

chart_btn = ctk.CTkButton(
    buttons,
    text="Show Charts",
    width=180,
    height=45,
    corner_radius=20,
    fg_color="#235347",
    hover_color="#163832",
    command=show_charts
)
chart_btn.grid(row=0,column=2,padx=15)


# ==========================
# Status Bar
# ==========================

status_label = ctk.CTkLabel(
    root,
    text="Status : Ready",
    height=35,
    fg_color="#0B2B26",
    text_color="#DAF1DE",
    font=("Segoe UI",14)
)

status_label.pack(fill="x",side="bottom")


# ==========================
# Update Dashboard Function
# ==========================

def update_dashboard():
    global df

    if df is None:
        return

    articles_card.configure(text=str(len(df)))

    if "category" in df.columns:
        category_card.configure(text=str(df["category"].nunique()))

    if "sentiment" in df.columns:
        positive_card.configure(
            text=str((df["sentiment"] == "Positive").sum())
        )

    accuracy = NewsClassifier().accuracy(df)
    accuracy_card.configure(text=f"{accuracy}%")

# ==========================
# Main Loop
# ==========================

root.mainloop()