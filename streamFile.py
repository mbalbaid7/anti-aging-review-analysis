import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from PIL import Image  # Import Image from Pillow
import streamlit as st


# تحميل البيانات من الملف
# df = pd.read_csv("c:/Users/User/Downloads/JS/File1.csv")
st.title("Anti Aging Product Review")
st.text("")
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


# طباعة أول 5 صفوف لفحص البيانات
# print(df.head())
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
# عرض ملخص سريع
    st.write("Total Reviews:", len(df))
    st.write("Average Rating Overall:", round(df['Rating'].mean(), 2))

# إضافة فلتر تفاعلي
    selected_product = st.selectbox("Select Product", df['Product'].unique())
    filtered_df = df[df['Product'] == selected_product]
    st.markdown(filtered_df.to_html(escape=False), unsafe_allow_html=True)

    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity
# تحليل المشاعر باستخدام TextBlob
    df['Sentiment'] = df['Review'].apply(get_sentiment)

# تصنيف المشاعر

    def label_sentiment(score):
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'

    df['Sentiment_Label'] = df['Sentiment'].apply(label_sentiment)

# تلوين الجدول حسب الشعور
    def highlight_status(row):
        if row['Sentiment_Label'] == 'Positive':
            return ['background-color: lightgreen'] * len(row)
        elif row['Sentiment_Label'] == 'Negative':
            return ['background-color: lightcoral'] * len(row)
        else:
            return ['background-color: '] * len(row)

    st.dataframe(df.style.apply(highlight_status, axis=1))

# # عدّ التقييمات حسب التصنيف
    sentiment_counts = df['Sentiment_Label'].value_counts()
# تصدير إلى اكسل
    import io

    if st.button("Download Results as Excel"):
        output = io.BytesIO()
        df.to_excel(output, index=False)
        st.download_button("Click to Download", output.getvalue(),
                           file_name="review_analysis.xlsx")

    if st.checkbox("Show/Hide \: Customer Sentiment Distribution"):
        # # رسم Pie Chart للمشاعر
        plt.figure(figsize=(6, 6))
        plt.pie(sentiment_counts, labels=sentiment_counts.index,
                autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightgray'])
        plt.title("Customer Sentiment Distribution")
# plt.show()
        st.pyplot(plt)
# # رسم WordCloud من التقييمات
    if st.checkbox("Show/Hide \: Word Cloud of Review Texts"):
        all_reviews = " ".join(df['Review'])
        wordcloud = WordCloud(width=800, height=400,
                              background_color='white').generate(all_reviews)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud of Review Texts")
# plt.show()
        st.pyplot(plt)

# # متوسط التقييمات لكل منتج
    if st.checkbox("Show/Hide \: Average Rating per Product bar chart"):
        avg_ratings = df.groupby("Product")[
            "Rating"].mean().sort_values(ascending=False)


# # رسم Bar Chart لأفضل المنتجات تقييماً
# # avg_ratings.plot(kind='bar', color='skyblue')
# # plt.title("Average Rating per Product")
# # plt.ylabel("Average Rating")
# # plt.xlabel("Product")
# # plt.xticks(rotation=45)
# # plt.tight_layout()
# # plt.show()
        fig, ax = plt.subplots()  # Create a figure and an axes object
        avg_ratings.plot(kind='bar', color='skyblue',
                         ax=ax)  # Plot on the axes object
        ax.set_title("Average Rating per Product")
        ax.set_ylabel("Average Rating")
        ax.set_xlabel("Product")
        plt.xticks(rotation=45)
        plt.tight_layout()
# plt.show()
# Display the plot in Streamlit
        st.pyplot(fig)
