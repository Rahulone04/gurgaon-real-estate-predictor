# Gurgaon Real Estate Price Predictor

[![Live App](https://img.shields.io/badge/Live%20App-AWS%20EC2-orange?style=for-the-badge&logo=amazon-aws)](http://13.61.34.49:8501)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![AWS EC2](https://img.shields.io/badge/AWS-EC2-yellow?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/ec2/)

## Live Demo
**[Click here to view the Live App](http://13.61.34.49:8501)**

---

## About the Project
A complete end-to-end Machine Learning project that predicts 
real estate property prices in Gurgaon, India. The project 
covers every stage of the data science pipeline — from raw 
web scraping to a live deployed web application.

---

## App Pages

| Page | Description |
|------|-------------|
| **Price Predictor** | Enter location, area, BHK and get predicted price instantly |
| **Analysis App** | Interactive charts, price heatmaps and location-based insights |
| **Recommend Apartments** | Get similar apartment suggestions using cosine similarity |

---

## Complete ML Pipeline
Web Scraping
↓
Data Cleaning & Merging (Flats + Houses + Land)
↓
Feature Engineering
↓
Exploratory Data Analysis (EDA)
↓
Outlier Detection & Missing Value Treatment
↓
Feature Selection
↓
Baseline Model → Model Selection
↓
Data Visualization & Insights
↓
Recommender System
↓
Deployed on AWS EC2

---

## 🗂️ Project Structure
gurgaon-real-estate-predictor/
|
├── 📁 1_Web_scraping/
│   └── scraping.py                          ← Scraped property listings
│
├── 📁 2_Data_cleaning/
│   ├── data-preprocessing of flat1-stage1.ipynb
│   ├── data-preprocessing-houses.ipynb
│   ├── data-preprocessing-houses-level1.ipynb
│   ├── data-preprocessing-level-2.ipynb
│   ├── merge-flats-and-house.ipynb          ← Merged all property types
│   ├── clean.py
│   └── [datasets: appartments, flats, houses, gurgaon_properties...]
│
├── 📁 3_feature Engineering/
│   ├── feature-engineering.ipynb            ← Created new features
│   └── [datasets]
│
├── 📁 4_EDA/
│   ├── eda-univariate-analysis.ipynb        ← Single variable analysis
│   ├── eda-multivariate-analysis.ipynb      ← Multi variable analysis
│   └── eda-pandas-profiling.ipynb           ← Auto profiling report
│
├── 📁 5_Outlier-Detection and removal/
│   ├── outlier-treatment.ipynb              ← IQR & z-score treatment
│   ├── missing-value-imputation.ipynb       ← Handled missing data
│   └── [datasets]
│
├── 📁 6_feature_selection and feture_engineering/
│   ├── feature-selection.ipynb              ← SelectKBest, correlation
│   └── feature-selection-and-feature-engineering.ipynb
│
├── 📁 7_base line_model/
│   └── baseline model.ipynb                ← Linear Regression benchmark
│
├── 📁 8_model Selection/
│   ├── model-selection.ipynb               ← Compared multiple models
│   └── df.pkl                              ← Processed dataframe
│
├── 📁 9_Data Visualization/
│   ├── Data-visualization.ipynb            ← Plotly & Seaborn charts
│   ├── latlong_screaper.py                 ← Scraped lat/long coordinates
│   └── [datasets with location data]
│
├── 📁 10_Recomender System/
│   └── Recomender System.ipynb             ← Cosine similarity engine
│
├── 📁 11_Insight_module/
│   └── insights-module.ipynb              ← Business insights & findings
│
└── 📁 Project/real-estate-app/            ← 🚀 LIVE STREAMLIT APP
├── home.py                            ← Main entry point
├── requirements.txt
├── df.pkl
├── pages/
│   ├── 1_price_predictor.py           ← Price prediction page
│   ├── 2_Analysis.App.py              ← Analytics dashboard
│   └── 3_Recommend_Appartments.py     ← Recommender page
└── Data/
├── cosine_sim1.pkl                ← Similarity matrix part 1
├── cosine_sim2.pkl                ← Similarity matrix part 2
├── cosine_sim3.pkl                ← Similarity matrix part 3
├── location_distance.pkl          ← Distance between locations
├── feature_text.pkl               ← Property text features
└── data_vi1.csv                   ← Visualization dataset

---

## Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.x |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Web Scraping** | BeautifulSoup, Requests |
| **App Framework** | Streamlit |
| **Deployment** | AWS EC2 (Ubuntu) |
| **Process Manager** | Systemd (auto-restart on crash/reboot) |
| **Version Control** | Git & GitHub |

---

## Models Evaluated

| Model | Type |
|-------|------|
| Linear Regression | Baseline |
| Ridge / Lasso | Regularized Linear |
| Decision Tree | Tree-based |
| Random Forest | Ensemble |
| Gradient Boosting | Boosting |
| XGBoost | Optimized Boosting |

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Rahulone04/gurgaon-real-estate-predictor.git

# 2. Go to app folder
cd gurgaon-real-estate-predictor/Project/real-estate-app

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download pipeline.pkl (see below) and place it here

# 5. Run the app
streamlit run home.py
```

---

## Model File (pipeline.pkl)

The trained model file `pipeline.pkl` (~140MB) exceeds GitHub's 
file size limit.

**[Download pipeline.pkl from Google Drive](YOUR_GOOGLE_DRIVE_LINK)**

After downloading, place it in: `Project/real-estate-app/`

---

## Deployment Details

| Item | Details |
|------|---------|
| **Platform** | AWS EC2 (Ubuntu 22.04) |
| **Instance** | t2.micro |
| **Port** | 8501 |
| **Process Manager** | Systemd service (always-on) |
| **Live URL** | http://13.61.34.49:8501 |

---

## Author

**Rahul**
- GitHub: [@Rahulone04](https://github.com/Rahulone04)
- Email: rahulone04@gmail.com

---



