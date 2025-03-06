import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Load the pre-trained model from TensorFlow Hub (Inception V3 model in this example)
model_url = "https://tfhub.dev/google/imagenet/inception_v3/classification/4"
model = hub.KerasLayer(model_url)

# Define a function to preprocess the image (resize, normalize, etc.)
def preprocess_image(image):
    image = cv2.resize(image, (299, 299))  # Resize to match Inception V3 input size
    image = image.astype(np.float32) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Open the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Preprocess the frame
    processed_frame = preprocess_image(frame)

    # Get model predictions
    predictions = model(processed_frame)

    # Get the predicted class label (index of the highest probability)
    predicted_class = np.argmax(predictions, axis=-1)

    # You can display the predicted class on the frame
    cv2.putText(frame, f"Predicted class: {predicted_class[0]}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the webcam feed with the prediction
    cv2.imshow('Webcam Feed', frame)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
