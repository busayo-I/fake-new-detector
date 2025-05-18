
import streamlit as st
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
import pandas as pd

# Setup
nltk.download('stopwords')
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Load model
model = joblib.load('fake_news_pipeline.pkl')

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

# App title
st.title("📰 Fake News Detection App")
st.write("This app uses **machine learning** to detect whether a news article is **Real** or **Fake**.")

# Tabs for functionality
tab1, tab2 = st.tabs(["📝 Single Prediction", "📁 Batch Prediction"])

# Tab 1: Single prediction
with tab1:
    user_input = st.text_area("Paste the news article content here...", height=200)
    if st.button("Predict", key="single"):
        if user_input.strip() == "":
            st.warning("Please enter the news article or headline.")
        else:
            cleaned = clean_text(user_input)
            prediction = model.predict([cleaned])[0]
            label = "🟢 This is a Real News" if prediction == 1 else "🔴 This is a Fake News"
            st.success(f"**Prediction:** {label}")

# Tab 2: Batch prediction
with tab2:
    st.write("Upload a CSV file with a column named `text` for batch prediction.")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if 'text' not in df.columns:
                st.error("The file must contain a `text` column.")
            else:
                df['cleaned'] = df['text'].apply(clean_text)
                df['prediction'] = model.predict(df['cleaned'])
                df['label'] = df['prediction'].apply(lambda x: "Real" if x == 1 else "Fake")
                st.write("✅ Prediction completed. Preview:")
                st.dataframe(df[['text', 'label']].head())

                # Download link
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Result CSV", data=csv, file_name="fake_news_predictions.csv", mime="text/csv")
        except Exception as e:
            st.error(f"Error processing file: {e}")

st.markdown("---")
st.markdown("Built with ❤️ for the 3MTT May 2025 Knowledge Showcase")