import cv2
import numpy as np
from samila import GenerativeImage,Projection
import matplotlib.pyplot as plt
import random
import time

def get_motion_level(prev_frame, curr_frame):
    # Convert to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(prev_gray, curr_gray)
    _, thresh = cv2.threshold(diff, thresh = 25, maxval = 255, type = cv2.THRESH_BINARY)
    motion_level = np.sum(thresh)
    return motion_level

def generate_samila_art(motion_level):
    normalized_motion = motion_level / 10000000.0

    def f1(x, y):
        return np.sin(x ** 2 + y) * normalized_motion + np.cos(x * y) * (1 - normalized_motion)

    def f2(x, y):
        return np.cos(y ** 2 - x) * normalized_motion + np.sin(x + y) * (1 - normalized_motion)

    g = GenerativeImage(f1, f2)
    g.generate()

    g.plot(projection = Projection.RANDOM,color="red", bgcolor="black", alpha=0.5)
    plt.title(f"Motion Level: {motion_level}")
    plt.show()

# Initialize webcam
v_cap = cv2.VideoCapture(0)
ret, prev_frame = v_cap.read()

print("Press 'q' to quit...")

last_art_time = time.time()
cooldown = 5

while True:
    ret, frame = v_cap.read()
    if not ret:
        break

    motion = get_motion_level(prev_frame, frame)
    prev_frame = frame.copy()

    # Show webcam feed
    cv2.putText(frame, f"Motion: {motion}", (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), thickness = 1)
    cv2.imshow("Webcam", frame)

    # Generate art if motion is strong and cooldown passed
    if motion > 5000 and (time.time() - last_art_time) > cooldown:
        print(f">!< Motion Detected: {motion}. Generating art...")
        generate_samila_art(motion)
        last_art_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

v_cap.release()
cv2.destroyAllWindows()
