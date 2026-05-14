import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.analyzer import analyze_portfolio
from utils.risk_model import risk_level
from utils.overlap import check_overlap
from utils.ai_recommendation import generate_ai_recommendations
from utils.report_generator import generate_pdf
from models.ml_model import train_model


# PAGE SETTINGS
st.set_page_config(
    page_title="Mutual Fund AI Analyzer",
    layout="wide"
)

# TITLE
st.title("Mutual Fund AI Health Analyzer")

st.write("Upload your Mutual Fund Portfolio CSV File")


# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


# MAIN LOGIC
if uploaded_file:

    # READ CSV
    df = pd.read_csv(uploaded_file)

    # CLEAN COLUMN NAMES
    df.columns = df.columns.str.strip()

    # SHOW DATA
    st.subheader("Uploaded Dataset")

    st.dataframe(df)

    # ANALYZE PORTFOLIO
    analysis = analyze_portfolio(df)

    # RISK LEVEL
    risk = risk_level(
        analysis["Average Risk"]
    )

    # CHECK OVERLAP
    overlap = check_overlap(df)

    # AI RECOMMENDATIONS
    recommendations = generate_ai_recommendations(df)

    # TRAIN ML MODEL
    (
        model,
        accuracy,
        report,
        encoder,
        regression_model,
        mae
    ) = train_model(df)

    # SUMMARY SECTION
    st.subheader("Portfolio Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Investment",
            f"₹{round(analysis['Total Investment'], 2)}"
        )

    with col2:

        st.metric(
            "Average Return",
            f"{round(analysis['Average Return'], 2)}%"
        )

    with col3:

        st.metric(
            "Health Score",
            round(analysis["Health Score"], 2)
        )

    # RISK ANALYSIS
    st.subheader("Risk Analysis")

    if risk == "Low Risk":

        st.success(risk)

    elif risk == "Moderate Risk":

        st.warning(risk)

    else:

        st.error(risk)

    # OVERLAP
    st.subheader("Fund Overlap")

    if overlap:

        st.write(overlap)

    else:

        st.write("No major overlap detected.")

    # AI RECOMMENDATIONS
    st.subheader("AI Recommendations")

    if recommendations:

        for rec in recommendations:

            st.info(rec)

    else:

        st.success(
            "Portfolio looks well balanced. No major issues detected."
        )

    # ML PREDICTION
    st.subheader("AI Portfolio Prediction")

    sample_data = [[
        analysis["Total Investment"],
        analysis["Average Return"],
        analysis["Average Risk"]
    ]]

    prediction = model.predict(sample_data)

    predicted_quality = encoder.inverse_transform(
        prediction
    )

    st.success(
        f"Predicted Portfolio Quality: {predicted_quality[0]}"
    )

    # MODEL ACCURACY
    st.subheader("ML Model Accuracy")

    st.write(
        f"Accuracy: {round(accuracy * 100, 2)}%"
    )

    # CLASSIFICATION REPORT
    st.subheader("Classification Report")

    st.text(report)

    # PIE CHART
    st.subheader("Investment Distribution")

    try:

        fig, ax = plt.subplots(figsize=(6, 6))

        ax.pie(
            df["Investment"],
            labels=df["Fund"],
            autopct="%1.1f%%"
        )

        ax.set_title("Investment Allocation")

        st.pyplot(fig)

    except Exception as e:

        st.error(f"Pie Chart Error: {e}")

    # PDF REPORT
    pdf_path = generate_pdf(
        analysis,
        risk,
        overlap,
        recommendations
    )

    # DOWNLOAD BUTTON
    with open(pdf_path, "rb") as file:

        st.download_button(
            label="Download AI Report PDF",
            data=file,
            file_name="MutualFundReport.pdf",
            mime="application/pdf"
        )

else:

    st.info("Please upload a CSV file to begin analysis.")