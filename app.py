import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

def main():
    st.title("Webcam Image Capture")

    # Initialize a placeholder for the captured image
    captured_image = st.empty()

    # WebRTC streamer configuration with error handling for NoneType
    webrtc_ctx = webrtc_streamer(
        key="webcam",
        video_frame_callback=video_frame_callback,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]}  # Google's public STUN server
            ]
        },
        media_stream_constraints={"video": True, "audio": False},
    )

    # Check if the context is properly initialized
    if webrtc_ctx.state.playing and webrtc_ctx.video_receiver:
        st.write("Webcam is live. Click 'Capture Image' to take a snapshot.")

        # Capture the image when the button is clicked
        if st.button("Capture Image"):
            try:
                # Get the current video frame as an image
                image = webrtc_ctx.video_receiver.get_frame().to_ndarray(format="bgr24")
                captured_image.image(image, channels="BGR", caption="Captured Image")
            except Exception as e:
                st.error(f"Error capturing image: {e}")
    else:
        st.warning("Webcam is not ready. Please check your network or STUN configuration.")

if __name__ == "__main__":
    main()
