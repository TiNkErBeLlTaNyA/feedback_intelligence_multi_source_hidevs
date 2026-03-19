import pandas as pd

def load_csv(path="data/sample_reviews.csv"):
    df = pd.read_csv(path)
    df['source'] = 'survey'
    return df