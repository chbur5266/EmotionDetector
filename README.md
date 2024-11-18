# Emotion Detector

This Emotion Detector is a Flask-based web application that uses computer vision to detect and analyze emotions in real-time via a webcam feed. Powered by OpenCV and the FER (Face Emotion Recognition) library, this app is perfect for interactive projects, streaming, or any application where gauging real-time emotional responses is valuable.

## Features

- **Real-Time Emotion Recognition**: Detects and analyzes facial expressions live through the webcam.
- **Dedicated Display Area**: Displays detected emotions in a non-obtrusive banner to maintain visibility of the main video content.
- **Multiple Emotion Detection**: Identifies various emotions and displays the predominant emotion with a confidence score.

## Built With

- [Python](https://www.python.org/) - The core programming language used.
- [Flask](https://palletsprojects.com/p/flask/) - The web framework for building the web app.
- [OpenCV](https://opencv.org/) - Used for handling video capture and image processing.
- [FER](https://github.com/justinshenk/fer) - A Python library for facial emotion recognition.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3.8 or higher
- pip
- Access to a webcam

### Installation

Clone the repository and install requirements:
   ```sh
   git clone https://github.com/chbur5266/EmotionDetector.git
   cd EmotionDetector
   pip install -r requirements.txt
```

Run the program:
```sh
python app.py
```

Open a web browser and navigate to:
http://localhost:5000/

The application should automatically access your webcam. Make sure to allow the necessary permissions to enable webcam use.

##Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request




