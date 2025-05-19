
# 📰 Fake News Detection App

This is an AI-powered Fake News Detection web application built using Python, Scikit-learn, and Streamlit. It uses Natural Language Processing (NLP) and a machine learning model (Logistic Regression with TF-IDF) to classify news headlines as **Real** or **Fake**.

## 🚀 Features

- Predict whether a news article is real or fake
- Easy-to-use web interface with Streamlit
- Trained on a dataset of real and fake news
- High accuracy (99% on test data)
- Deployable via Streamlit Cloud, Render, or local server

---

## 📁 Project Structure

```
📦 fake-news-detector/
├── fake_news_app.py           # Streamlit app
├── fake_news_pipeline.pkl     # Trained Logistic Regression model
├── fake_news_app_model.ipynb  # notebook of the train model
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🧠 Model Details

- **Algorithm**: Logistic Regression
- **Vectorizer**: TF-IDF (with bigrams)
- **Evaluation**: 99% accuracy on test set
- **Input**: News headlines or short articles
- **Output**: Prediction (Real or Fake)

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/busayo-I/fake-new-detector.git
cd fake-news-detector
```

2. **Create and Activate Virtual Environment (optional but recommended)**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
streamlit run fake_news_app.py
```

---

## 🌐 Deployment

You can deploy the app using:

- **[Streamlit Cloud](https://share.streamlit.io/)

---

## 📊 Example Inputs

| News Headline                                     |
|--------------------------------------------------|------------|
|The State House, Abuja President Tinubu Declares State of Emergency in Rivers State on Tuesday, March 18, 2025 | Real       |
| Pope endorses Trump for 2024 election            | Fake       |
|The Flying Eagles of Nigeria secured third place at the CAF U-20 Africa Cup of Nations Egypt 2025 with a dramatic 4-1 victory in a penalty shootout against tournament hosts Egypt on Sunday.               | Real       |
| president Tinubu sack all his ministers          | Fake       |

---

## 🧰 Tools & Libraries Used

- Python
- Streamlit
- Pandas & NumPy
- Scikit-learn
- NLTK
- TF-IDF Vectorizer
- Logistic Regression

---

## 🙌 Acknowledgements

- Dataset from [Kaggle Fake News Detection](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Inspired by real-world misinformation problems

---

## 📬 Contact

**Developer**: Ibrahim Ismail Busayo  
📧 Email: ibrahimbusayo2018@gmail.com  
🔗 LinkedIn: (https://www.linkedin.com/in/ismail-ibrahim-3a79b723a)

---
