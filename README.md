# MAGIC: Gamma vs. Hadron Classification

This repository contains a Jupyter/Colab notebook for the **classification of gamma-ray vs. hadron events** using machine learning techniques.  
The data comes from atmospheric Cherenkov telescope simulations, where the challenge is to distinguish **primary gamma rays (signal)** from **hadronic showers (background)** caused by cosmic rays.

---

## 📖 Project Overview

- Developed in **Google Colab** and saved in this repository as [`MAGIC.ipynb`](./MAGIC.ipynb).  
- Uses the **MAGIC gamma-ray telescope dataset**, which provides image parameters of Cherenkov showers (Hillas parameters and related features).  
- Goal: Build supervised machine learning models that can correctly classify events as **gamma** or **hadron**.

---

## ⚙️ Workflow

1. **Data Preprocessing**  
   - Cleaning and preparing the dataset  
   - Handling features relevant for classification  

2. **Exploratory Data Analysis (EDA)**  
   - Understanding class distribution  
   - Visualizing feature correlations  

3. **Model Training and Evaluation**  
   - Logistic Regression  
   - Decision Tree  
   - Random Forest  
   - (others can be added)  

4. **Performance Metrics**  
   - Accuracy  
   - Precision & Recall  
   - ROC-AUC  

---

## 🚀 Results

- Machine learning models can successfully discriminate between **gamma** and **hadron** events.  
- Ensemble methods (e.g., Random Forest) achieved higher performance compared to single models.  

---

## 📂 Repository Contents

- [`MAGIC.ipynb`](./MAGIC.ipynb) → Main notebook with code, analysis, and results  
- `README.md` → Project description  
