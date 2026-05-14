def generate_ai_recommendations(df):

    recommendations = []

    # HIGH RISK FUNDS
    high_risk = df[df["Risk"] > 7]

    # LOW RETURN FUNDS
    low_return = df[df["Return"] < 10]

    # CATEGORY CONCENTRATION
    concentration = df["Category"].value_counts()

    # -------------------------
    # HIGH RISK ANALYSIS
    # -------------------------

    if len(high_risk) > 0:

        risky_funds = ", ".join(
            high_risk["Fund"].head(3)
        )

        recommendations.append(
            f"High-risk exposure detected in: {risky_funds}. Consider reducing allocation in these funds."
        )

    # -------------------------
    # LOW RETURN ANALYSIS
    # -------------------------

    if len(low_return) > 0:

        low_return_funds = ", ".join(
            low_return["Fund"].head(3)
        )

        recommendations.append(
            f"Low-return funds detected: {low_return_funds}. Consider replacing them with better-performing funds."
        )

    # -------------------------
    # CATEGORY CONCENTRATION
    # -------------------------

    for category, count in concentration.items():

        if count > 3:

            recommendations.append(
                f"You have heavy concentration in {category} category ({count} funds). Diversification is recommended."
            )

    # -------------------------
    # PORTFOLIO EFFICIENCY
    # -------------------------

    avg_return = df["Return"].mean()

    avg_risk = df["Risk"].mean()

    if avg_return < 12:

        recommendations.append(
            "Portfolio return is below optimal level. Increasing exposure to quality growth funds may improve returns."
        )

    if avg_risk > 6:

        recommendations.append(
            "Portfolio volatility is high. Adding large-cap or index funds may improve stability."
        )

    # LIMIT RECOMMENDATIONS
    return recommendations[:5]