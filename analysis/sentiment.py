from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(str(text))
    c = score['compound']
    if c >= 0.05:
        return "positive", c
    elif c <= -0.05:
        return "negative", c
    return "neutral", c

def add_sentiment(df):
    df[['sentiment','confidence']] = df['text'].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )
    return df