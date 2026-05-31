#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pathlib import Path
import pandas as pd

class DataProcess:

    def __init__(self):
        self.data_dir = Path("./collected_data/")
        self.csv_files = list(self.data_dir.glob("*.csv"))
        self.all_columns = []

    def consolidated_stocks_data(self):
        consolidated_df = None

        for file in self.csv_files:
            try:
                # 1. Read both Date and ClosePrice columns
                df = pd.read_csv(file, usecols=['Date', 'ClosePrice'])

                # 2. Format the columns: Keep 'Date' as is, rename 'ClosePrice'
                ticker_name = file.stem.split('_')[0]
                df.columns = ['Date', f'CP_{ticker_name}'] 

                # 3. Combine the data
                if consolidated_df is None:
                    # First file initializes the main DataFrame
                    consolidated_df = df
                else:
                    # Subsequent files are merged side-by-side matching the 'Date' column
                    consolidated_df = pd.merge(consolidated_df, df, on='Date', how='outer')

            except Exception as e:
                print(f"Error processing file {file.name}: {e}")

        # 4. Optional: Sort rows by date so the final table is chronological
        if consolidated_df is not None:
            consolidated_df = consolidated_df.sort_values(by='Date').reset_index(drop=True)

            consolidated_df["Date"] = pd.to_datetime(consolidated_df["Date"], errors='coerce')

            numeric_col = consolidated_df.columns.drop('Date')

        for col in numeric_col:
            if consolidated_df[col].dtype == 'object':
                # Replace symbols, commas, and strip spaces
                consolidated_df[col] = consolidated_df[col].astype(str).str.replace(r'[$,%]', '', regex=True).str.replace(',', '')

        # 4. Now convert to numeric safely
        consolidated_df[numeric_col] = consolidated_df[numeric_col].apply(pd.to_numeric, errors='coerce')

        return consolidated_df




# In[ ]:




