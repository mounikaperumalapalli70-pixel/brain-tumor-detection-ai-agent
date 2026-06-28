from predict import predict_tumor

image_path = "uploads/test.jpg"   # Replace with an actual MRI image

result, confidence = predict_tumor(image_path)

print("Prediction:", result)

if confidence is not None:
    print("Confidence:", round(confidence, 2), "%")