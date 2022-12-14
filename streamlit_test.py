import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.write("# Real Time Sentiment Analysis")

user_input = st.text_input("Please rate our services >>: ")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write("Type something... ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")
    
# REF https://thecleverprogrammer.com/2021/03/19/streamlit-tutorial-using-python/
# input vocab has conditions for analysis