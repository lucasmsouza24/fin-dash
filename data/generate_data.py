import pandas as pd
import numpy as np

# creating fiction data
np.random.seed(42)
months = pd.date_range(start='2024-07-01', periods=12, freq='ME')
products = ['Produto A', 'Produto B', 'Produto C']
regions = ['North', 'South', 'East', 'West']

# creating main dataframe
data = []

for month in months:
    for product in products:
        for region in regions:
            revenue = np.random.randint(5000, 20000)
            expense = np.random.randint(2000, 15000)
            profit = revenue - expense
            data.append({
                'month': month,
                'product': product,
                'region': region,
                'revenue': revenue,
                'expense': expense,
                'profit': profit
            })

df_financeiro = pd.DataFrame(data)
df_financeiro.to_csv("./data.csv", index=False, encoding='utf-8')
