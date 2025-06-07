# 🖐️ Gesture Controlled Virtual Keyboard

A **real-time gesture-based virtual keyboard** using hand detection with OpenCV and CVZone. Control a full keyboard with just your hands — no physical contact required.

![keyboard demo banner](https://github.com/user-attachments/assets/28666bc8-10ce-4cbe-aa43-b4b7f3e127eb) 

---

## 📌 Features

- ✋ **Hand gesture recognition** using webcam
- 🧠 **Auto word suggestions** for faster typing
- 💾 **Save text to file** with Enter key
- 🔙 **Backspace functionality**
- 🌐 **Multilingual support-ready** (currently for English, can extend to Hindi)
- 🧠 Powered by **CVZone**, **OpenCV**, and **Pynput**

---

## 🧠 Tech Stack

- Python 🐍
- OpenCV 🎥
- CVZone 🧠
- Pynput ⌨️
- MediaPipe 🤖 (via CVZone internally)

---


## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/gesture-controlled-keyboard.git
cd gesture-controlled-keyboard

# Install required packages
pip install -r requirements.txt

------------------------------------------------------------------------------------------------------------------------------

🧠 How It Works
Uses your webcam to detect hand landmarks.

Tracks fingertip positions to determine key selection.

Pinching action (index + middle finger) triggers a key press.

Highlights keys being hovered or clicked.

Text typed is displayed on screen in real-time.

Press Enter to save the text to typed_text.txt.

------------------------------------------------------------------------------------------------------------------------------
📂 Folder Structure

gesture-controlled-keyboard/
│
├── main.py                # Main gesture keyboard script
├── typed_text.txt         # Output file for saved text
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies

------------------------------------------------------------------------------------------------------------------------------

🧠 Future Scope
🔄 Add gesture training via ML model

🌐 Toggle between English/Hindi typing

📱 Convert to mobile/AR version

🗣️ Add voice-to-text integration

------------------------------------------------------------------------------------------------------------------------------

🙋‍♂️ Author
Vijay Kumar Saini

🧑‍💻 Developer | Maker | Tech Explorer

📍 India

💡 Interested in HCI, AI, and gesture-based interfaces

⭐ Contribute / Feedback
If you like this project, give it a ⭐!
Feel free to open issues, suggest improvements, or submit pull requests.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

Let me know if you’d like a `requirements.txt` file generated or need the badge header (`stars`, `forks`, `MIT license`, etc.) added to this too.
