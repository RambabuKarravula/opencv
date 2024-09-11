import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

def main():
    st.title("Webcam Image Capture")

    webrtc_ctx = webrtc_streamer(
        key="webcam",
        video_frame_callback=video_frame_callback,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
    )

    if st.button("Capture Image"):
        if webrtc_ctx.video_receiver:
            image = webrtc_ctx.video_receiver.get_frame().to_ndarray(format="bgr24")
            st.image(image, channels="BGR", caption="Captured Image")
            # You can add code here to save the image if needed

if __name__ == "__main__":
    main()
