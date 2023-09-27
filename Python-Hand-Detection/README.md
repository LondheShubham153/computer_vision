# Python Hand Detection

This project uses Haar Feature-based Cascade Classifiers to detect hands in an image (or a frame from webcam).

For more information regarding using python for Haar Feature object detection see this link. 
(The detection code in this project was used from this link and altered to fit the project):
[Face Detection using Haar Cascades](https://docs.opencv.org/3.4/d7/d8b/tutorial_py_face_detection.html)

The haar-cascade used in this project was trained by github user [Aravindlivewire](https://github.com/Aravindlivewire/Opencv/blob/master/haarcascade/aGest.xml)

Note that this method of detecting hands in an image is nowhere near perfect. The accuracy of detection is highly dependent on the environment i.e. lighting, background movement, camera quality, etc. As well as the angle of the hand (detection works only when the palm is directly facing the camera).

The best environment is one with adequate lighting, but not too much, and a flat, unchanging background.
Test the program in a variety of environments to determine which works best for you.


## Detecting hands in python 3 using openCV

This project was written and tested in python 3.4+. 
Both required libraries are availble in python 2.7, but no testing was done in that version, so further maintenence will be required on your end to make it work in python 2.7.

You will need to install two python libraries for this project to work, opencv-python and imutils

You can install them using pip:
```
pip install opencv-python

pip install imutils
```
If any issues occur on installation, or for further information regarding these libaries, reference the documentation for each library:

[opencv-python](https://pypi.org/project/opencv-python/)

[imutils](https://github.com/jrosebr1/imutils)

If you need help using or installing pip see this link for help:
[Install pip for python](https://www.makeuseof.com/tag/install-pip-for-python/)

