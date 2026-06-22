from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, content):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Digital Forensic Investigation Report",
        styles["Title"]
    )

    elements.append(title)
    elements.append(Spacer(1, 20))

    paragraphs = content.split("\n")

    for line in paragraphs:

        if line.strip():

            elements.append(
                Paragraph(line, styles["BodyText"])
            )

            elements.append(
                Spacer(1, 8)
            )

    pdf.build(elements)