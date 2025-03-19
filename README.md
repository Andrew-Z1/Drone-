cat <<EOF > README.md
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
  - \`mediapipe\`
  - \`opencv-python\`
  - \`codrone-edu\`

### Installation
1. Clone the repository:
   \`\`\`sh
   git clone https://github.com/your-repo/hand-pose-drone-control.git
   cd hand-pose-drone-control
   \`\`\`
2. Install dependencies:
   \`\`\`sh
   pip install mediapipe opencv-python codrone-edu
   \`\`\`
3. Ensure your **drone is fully charged** and **Bluetooth is enabled** on your computer.

## 🛠 Usage
1. **Turn on** your Codrone EDU and place it on a safe surface.
2. **Run the script**:
   \`\`\`sh
   python hand_pose_drone_control.py
   \`\`\`
3. **Follow the on-screen prompts**:
   - A webcam window will open to detect your hand.
   - The drone **automatically takes off** when a hand is detected.
   - Perform gestures to control the drone.
4. **Press \`q\`** to exit. The drone will land automatically if it’s flying.

## 🎨 Example Output
\`\`\`
==================================================
🚀 Hand Pose Drone Control 🚀
==================================================

Drone connected. Ready for hand detection.
Hand detected, taking off...
Flying - UP
Moving drone UP
Flying - LEFT
Moving drone LEFT
Flying - FLIP
Performing FLIP
No hand detected, landing...
==================================================
Program terminated safely.
\`\`\`

## ⚠️ Error Handling
The program gracefully handles various errors, including:
- **Camera not found** (if \`cv2.VideoCapture(0)\` fails)
- **No drone connection** (ensuring Bluetooth and power are active)
- **Gesture misclassification** (may occur in poor lighting conditions)
- **Unexpected errors** with informative messages and automatic landing procedures

## 📜 License
This project is open-source under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute as needed.

## 💡 Future Improvements
- Enhanced **gesture set** for additional drone maneuvers
- Improved **gesture recognition** accuracy under various lighting conditions
- A **graphical user interface (GUI)** overlay for real-time gesture feedback
- Compatibility with multiple **Codrone models** or additional drones

---
🎉 **Control your drone with just a wave of your hand!**
EOF
