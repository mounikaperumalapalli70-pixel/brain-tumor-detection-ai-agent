import joblib
from preprocess import preprocess_image

# Load trained model and scaler
model = joblib.load("brain_tumor_model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_tumor(image_path):
    """
    Predict whether an MRI image contains a brain tumor.
    """

    # Preprocess image
    features = preprocess_image(image_path)

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)[0]

    # Confidence (if supported by the model)
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(features).max() * 100

    # Convert numeric prediction to label
    if prediction == 1:
        result = "Brain Tumor Detected"
    else:
        result = "No Brain Tumor"

    return result, confidence