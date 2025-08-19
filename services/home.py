import pandas as pd
from datetime import timedelta

def calculate_kpis(df: pd.DataFrame, period_filter: str):
    df["date"] = pd.to_datetime(df["month"])
    today = df["date"].max()

    if period_filter == "30d":
        start_date = today - timedelta(days=30)
    elif period_filter == "6m":
        start_date = today - pd.DateOffset(months=6)
    elif period_filter == "1y":
        start_date = today - pd.DateOffset(years=1)
    else:
        start_date = df["date"].min()  # fallback: não filtra nada

    filtered_df = df[df["date"] >= start_date]

    return {
        "revenue": filtered_df.revenue.sum(),
        "expense": filtered_df.expense.sum(),
        "profit": filtered_df.profit.sum()
    }
