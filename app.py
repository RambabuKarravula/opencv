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

    webrtc_ctx = webrtc_streamer(
        key="webcam",
        video_frame_callback=video_frame_callback,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]},
                {"urls": ["stun:stun.services.mozilla.com"]},
                {"urls": ["stun:stun.stunprotocol.org:3478"]},
                {"urls": ["stun:global.stun.twilio.com:3478"]}
            ]
        },
        media_stream_constraints={"video": True, "audio": False},
    )

    if st.button("Capture Image"):
        if webrtc_ctx.video_receiver:
            image = webrtc_ctx.video_receiver.get_frame().to_ndarray(format="bgr24")
            captured_image.image(image, channels="BGR", caption="Captured Image")
            # You can add code here to save the image if needed

    # Display the video feed continuously until an image is captured
    if webrtc_ctx.state.playing:
        st.write("Webcam is live. Click 'Capture Image' to take a snapshot.")

if __name__ == "__main__":
    main()
