Hand Pose Drone Control

📖 Overview

The Hand Pose Drone Control project allows you to control a Codrone EDU drone using real-time hand gesture recognition. By using MediaPipe Hands and OpenCV, this system identifies specific hand poses through your webcam and sends corresponding flight commands—such as taking off, moving up/down, left/right, hovering, and even performing a front flip.

✨ Features

Real-time gesture recognition via MediaPipe Hands
Automatic takeoff when a hand is detected
Automatic landing when no hand is detected
Custom gestures for Up, Down, Left, Right, Hover, and Flip
Intelligent command cooldown to prevent rapid or conflicting controls
Console feedback showing recognized commands and drone status
🚀 Getting Started

Prerequisites
Make sure you have:

Python 3.7+ (to support MediaPipe and Codrone EDU SDK)
A Codrone EDU and its Bluetooth connection set up
A working webcam for gesture detection
These Python packages installed:
mediapipe
opencv-python
codrone-edu
Installation
Clone or download the repository:
git clone https://github.com/your-repo/hand-pose-drone-control.git
cd hand-pose-drone-control
Install dependencies:
pip install mediapipe opencv-python codrone-edu
Ensure your drone is fully charged and Bluetooth is enabled on your computer.
🛠 Usage

Turn on your Codrone EDU and place it on a safe surface.
Run the script:
python hand_pose_drone_control.py
Follow the on-screen prompts:
A webcam window will open and begin detecting your hand.
When a hand is detected, the drone takes off automatically.
Use the designated hand poses to move or flip the drone.
Press q to stop the program. The drone will land automatically if it’s flying.
🎨 Example Output

Drone connected. Ready for hand detection.
Hand detected, taking off...
Flying - UP
Moving drone UP
Flying - LEFT
Moving drone LEFT
Flying - FLIP
Performing FLIP
No hand detected, landing...
Program terminated safely
⚠️ Error Handling

Camera not found: The script will report if it can’t access your webcam (cv2.VideoCapture(0) fails).
No drone connection: If pairing fails, ensure Bluetooth is on and that the Codrone EDU is powered.
Gesture misclassification: If lighting is poor or your hand is partially out of frame, the drone may hover or not respond.
Exceptions: All unexpected issues are caught, and the drone attempts to land safely before closing.
📜 License

This project is open-source under the MIT License. Feel free to modify and distribute as permitted.

💡 Future Improvements

Enhanced gesture set for more complex maneuvers
Refining detection algorithms for higher accuracy in low-light conditions
A user interface overlay for real-time gesture feedback
Support for multiple drones or additional Codrone models
🎉 Have fun commanding your drone with just a wave of your hand!