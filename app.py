import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Define a class for the video processing (just captures and shows the webcam feed)
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert the frame to a NumPy array
        return img  # Return the frame as-is

# Streamlit UI
st.title("Webcam Live Feed")
st.write("Click on start to access your webcam.")

# Start the webcam stream using streamlit-webrtc
webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
