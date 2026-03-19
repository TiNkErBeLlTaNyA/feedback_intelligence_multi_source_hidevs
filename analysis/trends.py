import pandas as pd

def sentiment_trend(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df.groupby([df['date'].dt.date, 'sentiment']).size().unstack().fillna(0)