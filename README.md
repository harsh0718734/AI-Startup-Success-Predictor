# 🚀 StartupSense AI
### Intelligent Decision-Support System for Startup Failure Prediction and Risk Evaluation

---

## 📁 Project Structure

```
startup_project/
├── app.py                    # Main entry point
├── auth.py                   # Authentication (login/signup/session)
├── database.py               # Data persistence (CSV-backed)
├── requirements.txt
├── data/
│   ├── india_startup.csv     # Master dataset (10,000 startups)
│   ├── startups_db.csv       # User-added startups (auto-created)
│   └── users.json            # User accounts (auto-created)
├── models/
│   ├── ml_models.py          # All ML logic (LR, RF, KNN, KMeans, MLR)
│   └── saved/                # Trained model artifacts (auto-created)
├── pages/
│   ├── owner_pages.py        # All Startup Owner tab renderers
│   └── investor_pages.py     # All Investor tab renderers
├── utils/
│   └── helpers.py            # Chart helpers, color palettes, feature lists
└── assets/
    └── logos/                # Uploaded startup logos (auto-created)
```

---

## ⚡ Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

### 3. Open in browser
```
http://localhost:8501
```

---

## 🔐 Demo Credentials

| Role           | Email                  | Password      |
|----------------|------------------------|---------------|
| Startup Owner  | owner@demo.com         | owner123      |
| Investor       | investor@demo.com      | investor123   |

---

## 🤖 Machine Learning Models

| Model                | Task                          | Library            |
|----------------------|-------------------------------|--------------------|
| Logistic Regression  | Failure classification        | scikit-learn       |
| Random Forest        | Failure classification (main) | scikit-learn       |
| K-Nearest Neighbors  | Failure classification        | scikit-learn       |
| K-Means              | Startup clustering (4 groups) | scikit-learn       |
| Multi-Linear Regr.   | Revenue growth forecasting    | scikit-learn       |

**Models are trained automatically on first use** and saved to `models/saved/`.

---

## 👤 Startup Owner Features

| Tab                | Description                                      |
|--------------------|--------------------------------------------------|
| 🏠 Home            | System overview and dataset statistics           |
| 📊 Dataset Explorer | Filter, search, sort, and download dataset     |
| 📈 Dashboard       | Overview charts, heatmap, sunburst, trends       |
| 🏢 Add Startup     | Form to register your startup with logo upload   |
| 🤖 Prediction      | Failure probability via 3 ML models + gauges     |
| 📉 Growth Forecast | Multi-year revenue growth prediction             |
| 💡 Recommendations | Rule + ML-based improvement suggestions          |
| ⚙️ Profile         | Account details and password change              |

## 💼 Investor Features

| Tab                  | Description                                    |
|----------------------|------------------------------------------------|
| 🏠 Home              | Ecosystem overview and funding stats           |
| 📂 All Startups      | Card grid with filters and search              |
| 📊 Startup Analysis  | Deep-dive with radar chart + 3-yr projection   |
| ⚖️ Comparison        | Side-by-side metrics + radar comparison        |
| 🤖 AI Chatbot        | Natural language startup Q&A                   |
| ⚙️ Profile           | Account details and password change            |

---

## 📊 Dataset Info

- **Source:** `india_startup.csv`
- **Records:** 10,000 Indian startups
- **Features:** 39 columns including funding, revenue, team size, scores, and status
- **Target:** `Startup_Status` (Active / Failed / Struggling / Acquired)
- **Risk Labels:** Low / Medium / High

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit + streamlit-option-menu
- **ML:** scikit-learn
- **Visualization:** Plotly
- **Data:** pandas, numpy
- **Persistence:** JSON (users), CSV (startups), joblib (models)
