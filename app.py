import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import tempfile
import os
from PIL import Image

# Directory to save captured images
save_folder = "captured_images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Define a class for the video processing
class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.img = None

    def transform(self, frame):
        self.img = frame.to_ndarray(format="bgr24")  # Convert the frame to a NumPy array
        return self.img

    def get_frame(self):
        return self.img

# Streamlit UI
st.title("Webcam Capture and Live Feed")

# Streamlit component for webcam
st.write("Click on 'Start' to access your webcam and capture an image.")

# Initialize video streamer
video_transformer = VideoTransformer()
webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=lambda: video_transformer)

# Button to capture the image
if st.button('Capture Image'):
    if video_transformer.get_frame() is not None:
        img = video_transformer.get_frame()
        # Save the image
        timestamp = st.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = os.path.join(save_folder, f"captured_image_{timestamp}.png")
        cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        st.success(f"Image captured and saved as {file_path}")
        # Show the captured image
        st.image(file_path, caption='Captured Image', use_column_width=True)
    else:
        st.error("No image to capture. Please start the webcam.")

