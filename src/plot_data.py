#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataPlot:

    def __init__(self):
        ...

    def pca_plot(
        self, 
        explained_variance_ratio,
        title, 
        xlabel, 
        ylabel,
    ):

        plt.figure(figsize = (10,5))

        components = [f"PC {i+1}" for i in range(8)]

        plt.bar(components, explained_variance_ratio[::-1] * 100, color='skyblue', label='Individual')
        # Plot cumulative explained variance line
        plt.plot(components, np.cumsum(explained_variance_ratio[::-1]) * 100, color='red', marker='o', label='Cumulative')
        plt.grid(True, linewidth = 0.2)

        plt.title(title , fontsize = 13, fontweight = "bold")
        plt.xlabel(xlabel, fontsize = 11)
        plt.ylabel(ylabel, fontsize = 11)

        plt.legend()
        plt.show()

    def heatmap_plot(
        self, 
        eigenvectors,
        title, 
        xlabel, 
        ylabel,
    ):

        df = pd.DataFrame(eigenvectors[:, ::-1], index=self.stock_names, columns=[f"PC {i+1}" for i in range(8)])

        plt.figure(figsize = (10,5))
        sns.heatmap(df, annot=True, cmap='coolwarm', center=0, fmt=".2f", linewidths=0.5)

        plt.title(title , fontsize = 13, fontweight = "bold")
        plt.xlabel(xlabel, fontsize = 11)
        plt.ylabel(ylabel, fontsize = 11)
        plt.show()

    def candlestics_plot(
        self, 
        df,
        title, 
        xlabel, 
        ylabel,
    ):

        plt.figure(figsize = (10,5))
        plt.plot(df)

        plt.title(title , fontsize = 13, fontweight = "bold")
        plt.xlabel(xlabel, fontsize = 11)
        plt.ylabel(ylabel, fontsize = 11)
        plt.show()


# In[ ]:




