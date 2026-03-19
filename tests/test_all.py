from analysis.sentiment import analyze_sentiment

def test_positive():
    s,_ = analyze_sentiment("good app")
    assert s == "positive"

def test_negative():
    s,_ = analyze_sentiment("bad app")
    assert s == "negative"