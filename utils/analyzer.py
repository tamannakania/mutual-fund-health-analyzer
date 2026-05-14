import pandas as pd

def analyze_portfolio(df):

    total_investment = df["Investment"].sum()

    avg_return = df["Return"].mean()

    avg_risk = df["Risk"].mean()

    diversification = len(df["Category"].unique())

    health_score = (
        (avg_return * 5)
        + (diversification * 10)
        - (avg_risk * 4)
    )

    health_score = max(0, min(100, int(health_score)))

    return {
        "Total Investment": total_investment,
        "Average Return": round(avg_return, 2),
        "Average Risk": round(avg_risk, 2),
        "Diversification": diversification,
        "Health Score": health_score
    }