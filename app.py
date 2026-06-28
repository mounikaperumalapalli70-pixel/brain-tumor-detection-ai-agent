import streamlit as st
import os

from predict import predict_tumor
from database import save_record
from report import generate_report

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Brain Tumor Detection AI Agent",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Brain Tumor Detection AI Agent")
st.write("Upload an MRI scan to detect the presence of a brain tumor using the trained Machine Learning model.")

st.markdown("---")

# -----------------------------
# Patient Details
# -----------------------------
st.subheader("👤 Patient Details")

patient_name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

st.markdown("---")

# -----------------------------
# Upload MRI
# -----------------------------
uploaded_file = st.file_uploader(
    "📤 Upload MRI Scan",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    image_path = os.path.join("uploads", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(
        uploaded_file,
        caption="Uploaded MRI Scan",
        width=350
    )

    if st.button("🔍 Analyze MRI"):

        with st.spinner("Analyzing MRI Scan..."):

            result, confidence = predict_tumor(image_path)

        # -----------------------------
        # Save Patient Record
        # -----------------------------
        save_record(
            patient_name,
            age,
            gender,
            result,
            confidence if confidence else 0
        )

        st.success("Analysis Completed")

        st.markdown("---")

        # -----------------------------
        # Prediction
        # -----------------------------
        st.subheader("Prediction")

        st.write(result)

        if confidence is not None:
            st.write(f"Confidence : {confidence:.2f}%")

        st.markdown("---")

        # -----------------------------
        # PDF Report
        # -----------------------------
        report_file = generate_report(
            patient_name,
            age,
            gender,
            result,
            confidence
        )

        with open(report_file, "rb") as pdf:

            st.download_button(
                label="📄 Download Diagnostic Report",
                data=pdf,
                file_name=f"{patient_name}_Report.pdf",
                mime="application/pdf"
            )

        st.markdown("---")

        # -----------------------------
        # Diagnostic Summary
        # -----------------------------
        st.subheader("Diagnostic Summary")

        if result == "Brain Tumor Detected":

            st.warning(
                """
The uploaded MRI scan contains imaging features that are consistent with a brain tumor.

This prediction has been generated using the trained Machine Learning model.

Please consult a neurologist or radiologist for professional medical diagnosis.
"""
            )

        else:

            st.success(
                """
No brain tumor was detected in the uploaded MRI scan.

This prediction should not replace professional medical diagnosis.
"""
            )

st.markdown("---")
st.caption("Brain Tumor Detection AI Agent | Developed using Streamlit + Machine Learning")