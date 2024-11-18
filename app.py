from flask import Flask, render_template, Response
import cv2
from fer import FER
import numpy as np


app = Flask(__name__)

# Initialize the video capture
video_capture = cv2.VideoCapture(0)
emotion_detector = FER()

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Add extra space for text at the top of the frame
        # Create a black banner of 60 pixels height at the top
        banner_height = 60
        frame_height, frame_width, channels = frame.shape
        banner = np.zeros((banner_height, frame_width, channels), dtype=np.uint8)
        frame_with_banner = cv2.vconcat([banner, frame])

        # Analyze the frame for emotions
        emotions = emotion_detector.detect_emotions(frame)
        if emotions:
            dominant_emotion = emotions[0]['emotions']
            emotion_label = max(dominant_emotion, key=dominant_emotion.get)
            emotion_score = dominant_emotion[emotion_label]

            # Set text specifications
            font_scale = 2  # Large font size for visibility
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_color = (255, 255, 255)  # White color
            font_thickness = 3

            # Calculate text size
            text = f'{emotion_label}: {emotion_score:.2f}'
            (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
            text_offset_x, text_offset_y = 10, banner_height - 10  # Adjust vertical position

            # Put text on the banner area
            cv2.putText(frame_with_banner, text, (text_offset_x, text_offset_y), font, font_scale, font_color, font_thickness)

        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', frame_with_banner)
        frame = buffer.tobytes()

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)