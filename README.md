# Real-Time Hand Gesture Recognition

Real-time hand gesture recognition using **Python, OpenCV and MediaPipe Hands**.

The application captures live video from a camera, detects a hand using MediaPipe, extracts **21 hand landmarks**, and classifies hand gestures using a rule-based approach.

## Recognized Gestures

The current implementation recognizes four gestures:

- OPEN HAND
- FIST
- VICTORY
- THUMBS UP

## Methodology

The processing pipeline is:

**Camera → OpenCV → MediaPipe Hands → 21 Hand Landmarks → Finger State Analysis → Gesture Classification → Live Output**

### Image Acquisition
OpenCV captures the live video stream from the camera.

### Hand Landmark Detection
Each frame is converted from BGR to RGB and processed by MediaPipe Hands. MediaPipe detects the hand and provides 21 landmark points.

### Finger State Analysis
The relative positions of the landmark points are used to determine whether the individual fingers are open or closed.

### Gesture Classification
A rule-based classification is used to recognize the gestures OPEN HAND, FIST, VICTORY and THUMBS UP.

### Visualization
OpenCV displays the hand landmarks and the recognized gesture directly on the live camera image.

## Technologies

- Python
- OpenCV
- MediaPipe Hands
- Computer Vision
- Rule-Based Gesture Classification

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run

Start the application:

```bash
python gesture.py
```

Press **Q** to close the application.

## Results

The implementation successfully performs real-time hand landmark detection and gesture recognition using the laptop camera.

The following gestures were successfully tested:

- OPEN HAND
- FIST
- VICTORY
- THUMBS UP

## Raspberry Pi 4

The project was also prepared for deployment on a Raspberry Pi 4. During the deployment, a boot-related technical problem occurred on the available Raspberry Pi board.

Therefore, the functionality and results are currently documented using the working laptop implementation. A test with another Raspberry Pi 4 is planned.

## Project

**EIM-E747.2 – Computer Vision in eingebetteten Systemen**  
HTWK Leipzig

## Author

**Salah Eddine Elhaibi**
