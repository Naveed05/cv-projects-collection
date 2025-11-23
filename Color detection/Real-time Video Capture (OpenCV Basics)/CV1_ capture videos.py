"""
PROJECT 1 — Real-time Video Capture using OpenCV

This script captures live video from the webcam and displays it on the screen.
Press ESC (27) to exit.
"""

import cv2

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

# Check if webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Show the live video
    cv2.imshow("Webcam Capture", frame)

    # Exit when ESC key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
