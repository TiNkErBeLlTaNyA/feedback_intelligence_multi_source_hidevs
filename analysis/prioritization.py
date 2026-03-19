from collections import Counter
import re

STOPWORDS = set([
    "the","is","and","to","i","a","my","it","of","in","for","on","this","that","why"
])

def extract_keywords(texts):
    words = []
    for t in texts:
        tokens = re.findall(r'\b\w+\b', str(t).lower())
        filtered = [w for w in tokens if w not in STOPWORDS and len(w) > 2]
        words += filtered
    return Counter(words)

def prioritize_issues(df):
    neg = df[df['sentiment']=="negative"]
    return extract_keywords(neg['text']).most_common(10)