# PORTFOLIO MANAGEMENT
Portfolio management is the process of selecting, organizing, monitoring, and adjusting investments to achieve specific financial goals while managing risk.


# PCA-Based Portfolio Risk Analysis

## Overview

This project is a quantitative portfolio risk analysis model built using Python, PCA (Principal Component Analysis), and Linear Algebra concepts.

The analysis uses **10 years of NSE stock market data** from **top-performing companies across different sectors** to study portfolio diversification and hidden market risk factors.

The main objective of this project was to understand whether a portfolio that appears diversified across sectors is actually diversified in terms of underlying market risk.

---

## Project Idea

As investors, we often assume that allocating investments equally across different sectors automatically creates a well-diversified portfolio.

However, after applying PCA and covariance-based risk analysis, this project demonstrates that:

- Even sector-diversified portfolios can still be heavily influenced by hidden common market factors
- Stocks from different sectors may still move together during periods of market stress
- A single dominant factor can explain a large portion of total portfolio risk

---

## Features

- Processes 10 years of historical NSE stock data
- Calculates daily logarithmic returns
- Builds covariance matrices to measure stock relationships
- Performs PCA using eigenvalues and eigenvectors
- Identifies hidden portfolio risk factors
- Measures:
  - Portfolio variance
  - Portfolio volatility
  - Annualized risk
  - Explained variance ratio
  - Risk contribution of principal components

---

## Concepts Used

- Portfolio Management
- Quantitative Finance
- Risk Analysis
- Covariance Matrix
- PCA (Principal Component Analysis)
- Eigenvalues & Eigenvectors
- Linear Algebra

---

## Key Insights

### 1. Hidden Market Factors Exist
Even though the portfolio contains top-performing stocks from different sectors, PCA revealed that common hidden market forces still dominate portfolio movement.

### 2. Sector Diversification Alone Is Not Enough
Holding stocks from multiple sectors does not always guarantee true diversification.

### 3. Correlation Increases During Stress
During volatile market conditions, stocks across sectors can become highly correlated.

### 4. First Principal Component Dominates Risk
The first principal component explained a significant portion of total portfolio volatility, indicating strong market-wide influence.

---


## Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn

---
