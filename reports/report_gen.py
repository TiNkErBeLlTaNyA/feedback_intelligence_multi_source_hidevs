from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(df):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Feedback Report", styles['Title']))
    content.append(Paragraph(f"Total: {len(df)}", styles['BodyText']))

    doc.build(content)