import feedparser
import pandas as pd

def fetch_app_store_reviews(app_id="389801252"):
    try:
        url = f"https://itunes.apple.com/rss/customerreviews/id={app_id}/sortby=mostrecent/json"
        feed = feedparser.parse(url)

        return pd.DataFrame([{
            "source": "app_store",
            "text": entry.title,
            "rating": int(entry.get("im_rating", 3)),
            "date": entry.published
        } for entry in feed.entries])
    except Exception as e:
        print("App Store error:", e)
        return pd.DataFrame()