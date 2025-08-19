import pandas as pd

def calculate_kpis(df: pd.DataFrame):
    return {
        "revenue": df.revenue.sum(),
        "expense": df.expense.sum(),
        "profit": df.profit.sum()
    }
