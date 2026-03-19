import sqlite3
import pandas as pd

DB = "data/feedback.db"

def save_to_db(df):
    # Ensure 'date' column exists before converting
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce') \
                        .dt.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB)
    df.to_sql("reviews", conn, if_exists="replace", index=False)
    conn.close()

def load_from_db():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT * FROM reviews", conn)
    conn.close()
    return df