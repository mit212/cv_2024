# Supplemental CV for Tim Detection

There are 2 main scripts in this repo. Both of them essentially find an HSV mask and get the largest contour in it. You can consider using either as a starting point for detecting where Tim is in the world, since Tim wears a solid maroon sweater. 

Sample photos of Tim are available in the `tim/` directory. Notice that the photos show Tim in various orientations, and have different color temperature and lighting conditions. Clone this repo and run `tim_test.py` to see how our CV algorithm works on these photos.

You can also run `real_time.py` to see how our CV algorithm works on live frames from your camera. Try holding up a single-colored object and tuning the HSV bounds for it. Note that it's better to keep the HSV bounds as loose as possible so you don't need to retune when lighting changes. The HSV mask does not need to be perfect to get a good contour and/or centroid. Once your bounds are set, try changing the orientation of the object and the lighting in the room and see if you can arrive at robust bounds.

Now that you can locate Tim's shirt in the frame, you still need to translate the pixel coordinates of the centroid into world coordinates. This will likely involve some calibration to calculate the homography matrix. There are many resources online on how to do this using OpenCV!
