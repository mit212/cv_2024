# Supplemental CV for Tim Detection

There are 2 main scripts in this repo. Both of them essentially apply an HSV mask and find the largest contour in it. You can consider using either as a starting point for detecting where Tim is in the world, since Tim wears a solid maroon sweater. 

Sample photos of Tim are in available the `tim/` directory. Notice that the photos show Tim in various orientations, and have different color temperature and lighting conditions. Clone this repo and run `tim_test.py` to see how our CV algorithm works on these photos.

You can also run `real_time.py` to see how our CV algorithm works on live frames from your camera. Try holding up a single-colored object and tuning the HSV bounds for it. Note that it's better to keep the HSV bounds as loose as possible so you don't need to retune when lighting changes. 

Now that you can find Tim's shirt in the frame, you still need to translate the pixel coordinates into world coordinates. This will likely involve some calibration to get the homography matrix. There should be many resources online on how to do this with OpenCV!