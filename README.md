# AI Startup Success Predictor & Market Analytics Hub

An interactive enterprise-grade Machine Learning ecosystem built during Semester 8 to evaluate, cluster, and forecast business viability parameters for emerging startups. The architecture integrates multiple pre-trained Scikit-Learn classifiers and clustering models into a unified Streamlit dashboard pipeline.

## 📌 Project Overview
This project functions as a cross-functional analytics hub that maps out a complete operational data lifecycle—taking raw investment history files and using pre-trained serial models to provide data-driven insights. It serves as an investigative dashboard for venture capitalists and startup owners to test structural business input criteria against trained machine learning boundaries.

## 🎯 Objectives
- Build a relational processing backend to clean, encode, and scale multidimensional transaction sets.
- Deploy an array of optimized machine learning classifiers including **Random Forest, K-Nearest Neighbors (KNN), and Logistic Regression** to forecast operational growth trajectories.
- Integrate **K-Means Clustering** algorithms to dynamically segment startups based on market sector parameters and funding levels.
- Author an interactive **Streamlit dashboard interface** to deliver seamless, real-time client testing environments.

## 🛠️ Tools & Technologies
- **Python (VS Code)** — Central software layer and runtime execution engine
- **Streamlit** — Web architecture framework used to build the front-end user control panels
- **Pandas & NumPy** — Array vector calculations, structural cleansing, and dataframe matrix styling
- **Scikit-Learn** — Custom categorical encoders, standard variable scaling (`scaler.pkl`), and core model training parameters
- **Pickle (`.pkl` serialization)** — Serialized storage framework used to deploy pre-trained analytical models cleanly without source recompilation overhead

## 📁 Architectural & Project File Tree
The directory is cleanly isolated into functional production tiers:
- `app.py` — The primary frontend execution script launching the core web engine.
- `auth.py` — Handles secure system onboarding validations and user profile state allocations.
- `database.py` — Establishes connection frameworks and reads persistent storage tables.
- `models/ml_models.py` — Houses class structures, query parsers, and evaluation mechanics.
- `models/saved/` — Contains pre-trained serialized model assets:
  - `scaler.pkl` — Normalized feature scaling parameters.
  - `feature_names.pkl` — Encoded variable matrix column schemas.
  - `random_forest.pkl`, `knn.pkl`, `logistic_regression.pkl` — Pre-fit classification weights.
  - `kmeans.pkl` — Customer/market segmentation boundary nodes.
- `data/` — Contains foundational transaction tables (`india_startup.csv`, `startups_db.csv`, `users.json`).
- `utils/helpers.py` — Text formatters, error-handling wrappers, and logging functions.

## 🚀 How to Run
1. Download the complete `startup_project` directory tree to your local workspace folder.
2. Initialize your terminal shell and verify that your system environment handles the required dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn streamlit
   ```
3. Boot up the unified multi-model interactive dashboard:
   ```bash
   streamlit run app.py
   ```
