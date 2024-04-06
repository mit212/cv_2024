### 2.12 Spring 2024 Supplemental CV 
### by Jinger Chong

from cv_functions import *
from tkinter import *

# Create scales for real-time adjustment of HSV bounds
# Similar to lab8_2024 morphOps.py but refactored
def create_gui():
    tk = Tk()

    scales = [
        ("Hue, lower", 0, 255, 160),
        ("Hue, upper", 0, 255, 180),
        ("Saturation, lower", 0, 255, 90),
        ("Saturation, upper", 0, 255, 255),
        ("Value, lower", 0, 255, 40),
        ("Value, upper", 0, 255, 135)
    ]

    tk_scales = []
    for label, from_, to, default in scales:
        scale = Scale(tk, from_=from_, to=to, label=label, orient=HORIZONTAL)
        scale.pack()
        scale.set(default)
        tk_scales.append(scale)

    return tk, tk_scales


tk, tk_scales = create_gui()

# Initialize default camera 
cap = cv2.VideoCapture(0)

while True:
    # Update scales
    tk.update()
    gui_values = np.array([tk_scale.get() for tk_scale in tk_scales])
    # Set HSV bounds to be values from scales
    lower_hsv = gui_values[::2]
    upper_hsv = gui_values[1::2]

    # Read from frame from camera
    _, img = cap.read()

    # Apply HSV mask and find largest contour in it
	# Function definition is in cv_functions.py
    cv2.imshow("Largest Contour within HSV Bounds", get_mask(img, lower_hsv, upper_hsv))
    cv2.waitKey(3)