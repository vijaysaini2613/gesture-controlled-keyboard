import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key
from time import sleep
import numpy as np

# Sample suggestion words (You can replace with a real dictionary)
suggestions_list = ["hello", "help", "helicopter", "how", "house", "hope", "world", "wonder", "work", "well", "what"]

# Webcam and detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
keyboard = Controller()

# Keyboard layout
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

suggestions = []
selected_language = "EN"  # Default to English

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

def draw_all_buttons(img, button_list):
    for button in button_list:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, 3)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
        font_scale = 2 if button.text in ["Space", "<", "Enter"] else 4
        offset = 20 if button.text not in ["Space", "<", "Enter"] else 15
        cv2.putText(img, button.text, (x + offset, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, font_scale, (255, 255, 255), 4)
    return img

def draw_textbox(img, text):
    cv2.rectangle(img, (50, 500), (1180, 600), (175, 0, 175), cv2.FILLED)
    text_show = text[-100:]  # Show last 100 characters
    cv2.putText(img, text_show, (60, 580),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    return img

def get_suggestions(current_text):
    words = current_text.strip().split(" ")
    if not words:
        return []
    last = words[-1]
    return [w for w in suggestions_list if w.startswith(last.lower())][:3]

# Create virtual buttons
button_list = []
for y_index, row in enumerate(keys):
    for x_index, key in enumerate(row):
        button_list.append(Button([100 * x_index + 50, 100 * y_index + 50], key))

# Add special keys
button_list.append(Button([400, 400], "Space", [250, 85]))
button_list.append(Button([700, 400], "<", [85, 85]))        # Backspace
button_list.append(Button([800, 400], "Enter", [120, 85]))   # Save text

final_text = ""
suggestion_buttons = []

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img, draw=True)
    img = draw_all_buttons(img, button_list)
    img = draw_textbox(img, final_text)

    # Show suggestions
    suggestions = get_suggestions(final_text)
    suggestion_buttons = []
    for i, word in enumerate(suggestions):
        x, y = 50 + i * 300, 620
        suggestion_buttons.append(Button([x, y], word, [280, 70]))
        cv2.rectangle(img, (x, y), (x + 280, y + 70), (0, 100, 255), cv2.FILLED)
        cv2.putText(img, word, (x + 20, y + 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    if hands:
        lmList = hands[0]["lmList"]
        if len(lmList) > 12:
            for button in button_list + suggestion_buttons:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    l, _, _ = detector.findDistance(tuple(lmList[8][:2]), tuple(lmList[12][:2]), img)
                    if l < 30:
                        key = button.text
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, key, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                        if key == "Space":
                            final_text += " "
                            keyboard.press(Key.space)
                        elif key == "<":
                            final_text = final_text[:-1]
                            keyboard.press(Key.backspace)
                        elif key == "Enter":
                            with open("typed_text.txt", "w", encoding="utf-8") as f:
                                f.write(final_text)
                            print("[✔] Text saved to 'typed_text.txt'")
                        elif key in suggestions:
                            words = final_text.strip().split(" ")
                            words[-1] = key
                            final_text = " ".join(words) + " "
                        else:
                            final_text += key
                            keyboard.press(key)
                        sleep(0.3)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
