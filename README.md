# Real-Time Hand Gesture Recognition

### Computer Vision Project | HTWK Leipzig

Real-time hand gesture recognition using **Python, OpenCV and MediaPipe Hands**.

The system processes a live camera stream, detects a hand and extracts **21 hand landmarks**. The relative positions of these landmarks are analyzed to determine finger states and classify different hand gestures in real time.

---

## System Pipeline

**Camera → OpenCV → BGR-to-RGB Conversion → MediaPipe Hands → 21 Hand Landmarks → Finger State Analysis → Gesture Classification → Live Output**

---

## Recognized Gestures

The current implementation recognizes four gestures:

| Gesture | Recognition Rule |
| :--- | :--- |
| **OPEN HAND** | Fingers are extended |
| **FIST** | Fingers are closed |
| **VICTORY** | Index and middle fingers are extended |
| **THUMBS UP** | Thumb is raised while the other fingers are closed |

---

## Methodology

### 1. Image Acquisition

OpenCV continuously captures frames from the camera.

### 2. Image Preprocessing

The camera frame is mirrored for intuitive interaction and converted from **BGR to RGB** before being processed by MediaPipe.

### 3. Hand Landmark Detection

**MediaPipe Hands** detects the hand and provides **21 landmark points** representing characteristic positions of the hand and fingers.

### 4. Finger State Analysis

Selected fingertip and joint landmarks are compared to determine whether individual fingers are extended or closed.

Examples of landmark pairs used in the implementation:

- Index finger: landmarks **8 and 6**
- Middle finger: landmarks **12 and 10**
- Ring finger: landmarks **16 and 14**
- Pinky finger: landmarks **20 and 18**

The thumb is evaluated separately using its landmark positions.

### 5. Gesture Classification

The calculated finger states are evaluated using a **rule-based classification**.

This allows the system to distinguish between **OPEN HAND**, **FIST**, **VICTORY** and **THUMBS UP**.

### 6. Real-Time Visualization

OpenCV displays the detected hand landmarks, their connections and the recognized gesture directly on the live camera image.

---

## Technologies

- **Python**
- **OpenCV**
- **MediaPipe Hands**
- Real-Time Computer Vision
- Landmark-Based Feature Extraction
- Rule-Based Classification

---

## Results

The implementation successfully performs real-time hand landmark detection and gesture recognition using the laptop camera.

### Example Results

<table>
<tr>
<td align="center"><b>VICTORY</b><br><img src="Bild%2010.09.26%20um%2001.21%20(1).png" width="420"></td>
<td align="center"><b>OPEN HAND</b><br><img src="Bild%2010.09.26%20um%2001.21.png" width="420"></td>
</tr>
<tr>
<td align="center"><b>THUMBS UP</b><br><img src="Bild%2010.09.26%20um%2001.22.png" width="420"></td>
<td align="center"><b>FIST</b><br><img src="Bild%2010.09.26%20um%2001.30.png" width="420"></td>
</tr>
</table>

---

## Raspberry Pi 4 Deployment

The project is designed for deployment on a **Raspberry Pi 4** with a camera.

During the current deployment phase, a boot-related technical problem occurred with the available Raspberry Pi board. Therefore, the software functionality was validated using the working laptop implementation.

A deployment test with another Raspberry Pi 4 is planned.

---

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run

Start the application:

```bash
python gesture.py
```

Press **Q** to stop the application.

---

## Project Structure

```text
hand-gesture-recognition/
│
├── gesture.py
├── requirements.txt
├── README.md
└── result images
```

---

## Course

**EIM-E747.2 – Computer Vision in eingebetteten Systemen**  
HTWK Leipzig

## Author

**Salah Eddine Elhaibi**
