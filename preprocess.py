import cv2
import numpy as np
from skimage.feature import hog

IMG_SIZE = 128

def preprocess_image(image_path):
    """
    Load MRI image and preprocess it
    """

    # Read image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("Image not found!")

    # Resize image
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    # Extract HOG features
    features = hog(
        image,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys"
    )

    return np.array(features).reshape(1, -1)