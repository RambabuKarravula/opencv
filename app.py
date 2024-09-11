import cv2
import os
import streamlit as st
from datetime import datetime
from PIL import Image

# Create a folder to store the images if it doesn't exist
save_folder = "captured_images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Function to capture an image using the webcam
def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return None

    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = os.path.join(save_folder, f"image_{timestamp}.png")
        cv2.imwrite(file_name, frame)
        cap.release()
        return file_name
    else:
        st.error("Error: Could not capture image.")
        cap.release()
        return None

# Streamlit app
st.title("Image Capture and Search")

# Button to capture the image
if st.button("Capture Image"):
    file_name = capture_image()
    if file_name:
        st.success(f"Image saved as {file_name}")
        st.image(file_name, caption="Captured Image", use_column_width=True)

# Option to search and display an existing image
if st.button("Search Image"):
    image_files = [f for f in os.listdir(save_folder) if f.endswith(".png")]
    
    if len(image_files) > 0:
        selected_image = st.selectbox("Select an image", image_files)
        image_path = os.path.join(save_folder, selected_image)
        st.image(image_path, caption=f"Displaying: {selected_image}", use_column_width=True)
    else:
        st.warning("No images found.")
