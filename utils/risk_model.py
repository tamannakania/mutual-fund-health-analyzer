def risk_level(avg_risk):

    if avg_risk <= 3:
        return "Low Risk"

    elif avg_risk <= 6:
        return "Moderate Risk"

    else:
        return "High Risk"