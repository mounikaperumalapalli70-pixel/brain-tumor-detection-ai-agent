from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generate_report(name, age, gender, prediction, confidence):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{name}_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Brain Tumor Diagnostic Report</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Patient Name:</b> {name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Age:</b> {age}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Gender:</b> {gender}", styles["BodyText"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Prediction:</b> {prediction}", styles["BodyText"]))

    if confidence is not None:
        story.append(
            Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["BodyText"])
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    if prediction == "Brain Tumor Detected":
        summary = """
        The uploaded MRI scan contains imaging features consistent
        with a brain tumor.

        This prediction is generated using the trained Machine
        Learning model.

        Please consult a neurologist or radiologist for further
        medical evaluation.
        """
    else:
        summary = """
        No brain tumor was detected in the uploaded MRI scan.

        However, this prediction should not replace a
        professional medical diagnosis.
        """

    story.append(Paragraph("<b>Diagnostic Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Italic"],
        )
    )

    doc.build(story)

    return filename