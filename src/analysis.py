#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('run', 'data_process.ipynb')
get_ipython().run_line_magic('run', 'plot_data.ipynb')

import pandas as pd
import numpy as np

class Analysis(DataProcess, DataPlot):

    def __init__(self):
        super().__init__()
        self.covariance_matrix = None
        self.weights = np.repeat(0.125, 8)
        self.explained_variance_ratio = None
        self.eigenvalues = None
        self.eigenvectors = None
        self.stock_names = ["ABBOTINDIA", "BAJAJFINSV", "CORONA", "HAL", "HCLTECH", "JPPOWER", "M&M", "RELIANCE"]

    def returns(self):
        df = self.consolidated_stocks_data()
        # Returns
        # This strips out 'Date', 'timestamp', or string columns completely
        df_np = df.select_dtypes(include=[np.number])

        price_ratios = df_np / df_np.shift(1)
        log_returns = np.log(price_ratios)
        log_returns.columns = [f'r_{col}' for col in df_np.columns]

        df_np = df_np.join(log_returns)

        cols_to_drop = [
            'CP_ABBOTINDIA', 'CP_BAJAJFINSV', 'CP_CORONA', 'CP_HAL', 
            'CP_HCLTECH', 'CP_JPPOWER', 'CP_M&M', 'CP_RELIANCE']

        # 2. Drop them all instantly in place
        df_np.drop(columns=cols_to_drop, inplace=True)

        return df_np


    def calculation(self):
        df = self.returns()

        self.covariance_matrix = df.cov()
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(self.covariance_matrix)

        # print("Covarience Matrix:")
        # print(covariance_matrix)
        # print("Eigenvalues (Lambda):")
        # print( self.eigenvalues)

        # print("\nEigenvectors (v) Matrix Shape:")
        # print(self.eigenvectors.shape)

        total_variance = np.sum(self.eigenvalues)
        self.explained_variance_ratio = self.eigenvalues/ total_variance

        loading_df = pd.DataFrame(
        self.eigenvectors[:, ::-1],
        index=self.stock_names,
        columns=[f'PC{i+1}' for i in range(8)]
        )

        print(loading_df.round(4))

        # PCA Visualization
        self.pca_plot(
            self.explained_variance_ratio,
            "Portfolio Risk Factors Breakdown",
            "Hidden Factors",
            "Percentage of Risk Explained (%)"
        )

        # Heat Map Visualization
        self.heatmap_plot(
            self.eigenvectors,
            "Eigenvector Heatmap: How Stocks Map to Risk Factors",
            "Risk Factors (PC1 = Main Market Force)",
            "Stocks"
        )

        # Calculate the overall profit (Scalar value)
        portfolio_return = self.weights @ self.covariance_matrix * 100

        # Annualised Portfolio Return (Linear scaling)
        portfolio_return_annual = portfolio_return * 252 * 100

        # Calculate the overall risk baseline (Scalar value)
        portfolio_variance = self.weights.T @ self.covariance_matrix @ self.weights

        # Annualised Portfolio Variance (Linear scaling)
        portfolio_variance_annual = portfolio_variance * 252

        # Calculate the actual daily risk percentage (Standard Deviation)
        portfolio_volatility = np.sqrt(portfolio_variance)  

        # Annualised Portfolio Volatility (Scaled by the SQUARE ROOT of time)
        portfolio_volatility_annual = portfolio_volatility * np.sqrt(252)

        print(f"The primary risk factor explains {self.explained_variance_ratio[-1]*100:.2f}% of all portfolio risk.")


        data = {
                "portfolio_return": portfolio_return, 
                "portfolio_return_annual":portfolio_return_annual, 
                "portfolio_variance": portfolio_variance, 
                "portfolio_variance_annual":portfolio_variance_annual,
                "portfolio_volatility":portfolio_volatility,
                "portfolio_volatility_annual":portfolio_volatility_annual,
               }

        # Presenting the Usefull Data
        self.present(data)


    def present(self, data):
        df = pd.DataFrame({
        'Weight (%)': self.weights * 100,
        'Daily Return (%)': data['portfolio_return'] * 100,
        'Annual Return (%)': data['portfolio_return_annual']
        })

        # Clean index names (removes 'r_CP_')
        df.index = df.index.str.replace('r_CP_', '')

        print("--- Asset Breakdown ---")
        print(df.round(2))

        print("\n--- Portfolio Risk Metrics ---")
        print(f"Annual Risk (Volatility): {data['portfolio_volatility_annual']*100:.2f}%")


# In[ ]:




