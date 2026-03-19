# Multi-Source Feedback Intelligence System

## 🚀 Overview  
The Feedback Intelligence System is a Python-based analytics platform designed to collect, process, and analyze customer feedback from multiple sources such as Google Play Store, App Store, and survey CSV files. It transforms raw feedback into actionable insights using sentiment analysis, trend detection, and issue prioritization.

---

## 🎯 Key Features  

- 🔗 Multi-source data integration (Google Play, App Store, CSV)  
- 😊 Sentiment analysis with confidence scoring  
- 📈 Trend analysis over time  
- ⚠️ Issue detection from negative feedback  
- 📊 Interactive Streamlit dashboard  
- ☁️ WordCloud visualization  
- 📄 Automated PDF report generation  
- 🌐 REST API with FastAPI (Swagger UI)  
- 🗄️ SQLite database for storage  

---

## 🏗️ System Architecture  

Data Sources → Data Processing → Database → Dashboard & API → Reports  

---

## 🛠️ Tech Stack  

- Python  
- Pandas  
- Streamlit  
- FastAPI  
- SQLite  
- VADER Sentiment Analysis  
- ReportLab  

---

## ⚙️ Installation  

```bash
git clone <your-repo-link>
cd feedback_intelligence
pip install -r requirements.txt
```

---

## ▶️ Running the Project  

### Step 1: Run Data Pipeline  
```bash
python main.py
```

### Step 2: Launch Dashboard  
```bash
streamlit run dashboard/app.py
```

### Step 3: Run API  
```bash
uvicorn api.main:app --reload
```

---

## 🌐 API Documentation  

After running the API, open:

```
http://127.0.0.1:8000/docs
```

Available endpoints:
- `/summary` → Sentiment distribution  
- `/issues` → Top recurring issues  
- `/sources` → Feedback source breakdown  

---

## 📊 Dashboard Features  

- KPI metrics (Total, Positive %, Negative %)  
- Sentiment trend visualization  
- Recurring issue detection  
- WordCloud for negative feedback  
- PDF report generation  

---

## 📄 Report Generation  

Generates a weekly PDF report including:
- Total feedback count  
- Sentiment distribution  
- Key insights  

---

## 🎥 Demo Video  

[Click here to watch demo](https://youtu.be/NnOj7TezYzg)

---

## 📈 Use Case  

This system helps product managers and businesses:
- Monitor customer satisfaction  
- Detect bugs and complaints early  
- Improve product quality using data-driven insights  

---

## 🧪 Testing  

```bash
pytest --cov=.
```

---

## 📌 Outcome  

A complete, production-style feedback analysis system capable of processing real-world data, generating insights, and supporting business decision-making.
