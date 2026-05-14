from fpdf import FPDF

def generate_pdf(data, risk, overlap, recommendations):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Mutual Fund AI Analyzer Report", ln=True)

    pdf.ln(10)

    for key, value in data.items():

        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.cell(200, 10, txt=f"Risk Level: {risk}", ln=True)

    pdf.ln(5)

    pdf.cell(200, 10, txt="Fund Overlap:", ln=True)

    for key, value in overlap.items():

        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.ln(5)

    pdf.cell(200, 10, txt="Recommendations:", ln=True)

    for rec in recommendations:

        pdf.multi_cell(0, 10, rec)

    path = "reports/mutual_fund_report.pdf"

    pdf.output(path)

    return path