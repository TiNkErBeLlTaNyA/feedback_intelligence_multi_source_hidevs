from google_play_scraper import reviews, Sort
import pandas as pd

def fetch_google_reviews(app_id="com.instagram.android", count=100):
    try:
        result, _ = reviews(app_id, lang='en', country='in', sort=Sort.NEWEST, count=count)
        return pd.DataFrame([{
            "source": "google_play",
            "text": r['content'],
            "rating": r['score'],
            "date": r['at']
        } for r in result])
    except Exception as e:
        print("Google API error:", e)
        return pd.DataFrame()