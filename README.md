
# 🧪 Anti-Aging Product Review Analyzer

An interactive data analysis app built using Python and Streamlit. This project analyzes customer reviews of anti-aging products to extract insights through sentiment analysis, word clouds, and visual charts.

## 📊 Features

- Upload your own CSV file with product reviews
- Sentiment analysis using TextBlob
- Sentiment classification (Positive, Neutral, Negative)
- Interactive filters by product
- Word cloud generation for frequent terms
- Pie chart of sentiment distribution
- Bar chart of average product ratings
- Highlighted tables based on sentiment

## 🗂️ Sample Data Format

Your CSV file should include the following columns:

```csv
Product,Review,Rating,Date
Collagen Plus,"Amazing product, worked great!",5,2024-12-01
CoQ10,"Didn’t work for me.",2,2024-12-05
...
```

## ▶️ How to Run the App

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/anti-aging-review-analysis.git
cd anti-aging-review-analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

3. Run the Streamlit app:

```bash
streamlit run streamFile.py
```

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- TextBlob
- WordCloud
- Streamlit

## 📸 Screenshots

![Preview](https://github.com/mbalbaid7/anti-aging-review-analysis/tree/main/Anti_Aging_Analyzer.png?raw=true)


## 🔗 Author

Created by [Maryam Balbaid]  
GitHub: https://github.com/mbalbaid7

---

Feel free to contribute or fork this project if you found it useful!
