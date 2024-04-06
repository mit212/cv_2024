### 2.12 Spring 2024 Supplemental CV 
### by Jinger Chong

import cv2
import numpy as np

# Calculate the centroid of the contour
def get_centroid(contour):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return (cx, cy)


# Apply HSV mask and find largest contour in it
def get_mask(img, lower_hsv, upper_hsv):

    # Create a mask of only pixels with HSV within bounds
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_mask = cv2.inRange(img_hsv, lower_hsv, upper_hsv)

    # Simple circle kernel
    kernel = np.array([[0, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0]], dtype=np.uint8)
    # Morphological operations to close holes 
    closed_mask = cv2.morphologyEx(hsv_mask, cv2.MORPH_CLOSE, kernel, iterations = 2)

    # Dim regions of original image outside mask
    result = img.copy()
    result[closed_mask == 0] = 0
    result = cv2.addWeighted(img, 0.25, result, 0.75, 0)

    # Find parent contours in mask
    contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # If any contour found
    if len(contours) != 0:
        # Choose the contour with the largest area
        largest_contour = max(contours, key=cv2.contourArea)
        # Draw this contour 
        cv2.drawContours(result, [largest_contour], -1, (0, 255, 255), 2)
        # Get the centroid of this contour
        centroid = get_centroid(largest_contour)
        if centroid is not None:
            # Draw a circle at the centroid
            cv2.circle(result, (centroid[0], centroid[1]), 2, (0, 255, 0), -1)
    
    # Return annotated version of original image for visualization
    return result
