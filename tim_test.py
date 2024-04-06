### 2.12 Spring 2024 Supplemental CV 
### by Jinger Chong

from cv_functions import *
import os
import cv2

# Manually tuned using lab8_2024 colorThresh.py
# to identify Tim's red shirt
lower_red = np.array([160, 90, 40])
upper_red = np.array([180, 255, 135])

input_path = "tim"
output_path = "results"

# Create output folder if doesn't exist yet
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Go through all images in input folder
files = os.listdir(input_path)
for file in files:
	if file.endswith('.jpg') or file.endswith('.png'):
		img = cv2.imread(os.path.join(input_path, file))
		# Apply HSV mask and find largest contour in it
		# Function definition is in cv_functions.py
		result = get_mask(img, lower_red, upper_red)
		# Save as image with same name under output folder
		cv2.imwrite(os.path.join(output_path, file), result)