cat << 'EOF' > README.md
# Hand Pose Drone Control

## 📖 Overview
The **Hand Pose Drone Control** project enables users to control a **Codrone EDU** drone using real-time hand gestures. By utilizing [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) and [OpenCV](https://opencv.org/), the system detects specific hand poses via a webcam and translates them into drone flight commands such as takeoff, movement, hovering, and flips.

## ✨ Features
- **Real-time gesture recognition** using MediaPipe Hands
- **Automatic takeoff** when a hand is detected
- **Automatic landing** when no hand is detected
- **Custom gestures** for Up, Down, Left, Right, Hover, and Flip
- **Built-in cooldown system** to prevent rapid or conflicting commands
- **Real-time console feedback** on recognized commands and drone status

## 🚀 Getting Started

### Prerequisites
Ensure your system meets the following requirements:
- **Python 3.7+** (to support MediaPipe and the Codrone EDU SDK)
- A **Codrone EDU** drone with Bluetooth connectivity
- A **working webcam** for gesture detection
- Required dependencies:
  - `mediapipe`
  - `opencv-python`
  - `codrone-edu`

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/hand-pose-drone-control.git
   cd hand-pose-drone-control
