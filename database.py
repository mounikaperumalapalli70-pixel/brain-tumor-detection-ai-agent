import pandas as pd
import os
from datetime import datetime

FILE_NAME = "records/patient_records.csv"


def save_record(name, age, gender, prediction, confidence):

    data = {
        "Patient Name": name,
        "Age": age,
        "Gender": gender,
        "Prediction": prediction,
        "Confidence (%)": round(confidence, 2) if confidence else "N/A",
        "Date": datetime.now().strftime("%d-%m-%Y"),
        "Time": datetime.now().strftime("%H:%M:%S")
    }

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_csv(FILE_NAME, index=False)