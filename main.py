import pandas as pd
from fetchers.google_play import fetch_google_reviews
from fetchers.app_store import fetch_app_store_reviews
from fetchers.csv_loader import load_csv
from analysis.sentiment import add_sentiment
from utils.db import save_to_db

def run():
    g = fetch_google_reviews()
    a = fetch_app_store_reviews()
    c = load_csv()

    df = pd.concat([g,a,c], ignore_index=True)
    df = add_sentiment(df)

    save_to_db(df)
    df.to_csv("data/reviews.csv", index=False)

    print("Done")

if __name__ == "__main__":
    run()