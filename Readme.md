# OpenCV with Python

## 📌 About This Project

This project is a collection of my **Python and OpenCV learning programs**.
I created and practiced different concepts related to **image processing, image manipulation, video processing, and webcam access** using OpenCV.

The purpose of this project is to understand the fundamentals of **Computer Vision with Python** and build a strong foundation for future projects in Image Processing, Computer Vision, and AI/ML.



## 🛠️ Technologies Used

* **Python**
* **OpenCV (`cv2`)**
* **PyCharm**
* **NumPy**


## 📚 Topics Covered

### 1. Installing OpenCV

* Installing OpenCV using `pip`
* Importing OpenCV in Python
* Checking the OpenCV version

### 2. Open vs OpenCV

* Difference between the general concept of **open** and **OpenCV**
* Understanding OpenCV as a computer vision library

### 3. Reading an Image

* Loading an image using OpenCV
* Displaying an image
* Understanding image paths

### 4. Writing an Image

* Saving processed images
* Writing images to a specified location

### 5. Resizing an Image

* Changing image width and height
* Understanding image dimensions
* Using `cv2.resize()`

### 6. Morphological Operations

Practiced basic morphological image processing operations such as:

* Erosion
* Dilation
* Opening
* Closing

### 7. Flipping an Image

* Horizontal flipping
* Vertical flipping
* Flipping an image using `cv2.flip()`

### 8. Resizing Based on Aspect Ratio

* Understanding aspect ratio
* Maintaining the original proportions of an image
* Resizing images without distortion

### 9. Adding Shapes and Text

Practiced drawing on images using:

* Lines
* Rectangles
* Circles
* Polygons
* Text

### 10. Shifting an Image

* Moving an image horizontally and vertically
* Understanding translation
* Using transformation matrices

### 11. Image Rotation

* Rotating images around a specific point
* Understanding rotation matrices
* Using OpenCV rotation functions

### 12. Thresholding

Practiced image thresholding techniques for separating objects from the background.

Concepts include:

* Binary thresholding
* Grayscale thresholding
* Different thresholding methods

### 13. Gaussian Blur

* Understanding image smoothing
* Reducing noise
* Using Gaussian filtering

### 14. Median Blur

* Removing noise from images
* Understanding median filtering
* Using `cv2.medianBlur()`

### 15. Bilateral Filter

* Smoothing images while preserving edges
* Understanding edge-preserving filtering
* Using `cv2.bilateralFilter()`

### 16. Edge Detection

* Detecting edges in images
* Understanding the importance of edges in Computer Vision
* Practicing edge detection using OpenCV

### 17. Reading a Video

* Opening a video file
* Reading video frames
* Displaying video frames
* Detecting when the video ends

### 18. Writing a Video

* Creating a video file
* Writing processed frames into a video
* Understanding video codecs and frame rates

### 19. Accessing the Webcam

* Accessing the computer's webcam
* Capturing live frames
* Displaying the webcam feed
* Releasing the webcam properly

---

## 📂 Project Structure


OpenCV-Python/
│
├── images/
│   ├── input/
│   └── output/
│
├── videos/
│   ├── input/
│   └── output/
│
├── image_read.py
├── image_write.py
├── image_resize.py
├── morphological_operations.py
├── image_flip.py
├── aspect_ratio_resize.py
├── shapes_and_text.py
├── image_shift.py
├── image_rotation.py
├── thresholding.py
├── gaussian_blur.py
├── median_blur.py
├── bilateral_filter.py
├── edge_detection.py
├── video_read.py
├── video_write.py
├── webcam.py
│
└── README.md


> The filenames above are examples. They can be changed according to the actual filenames in the project.

---

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your system.

Check the installed version:

```bash
python --version
```

### 2. Install OpenCV

Open the PyCharm terminal or Command Prompt and run:

```bash
pip install opencv-python
```

### 3. Install NumPy

```bash
pip install numpy
```

### 4. Verify OpenCV Installation

Run:


import cv2

print(cv2.__version__)

If the OpenCV version is displayed, OpenCV has been successfully installed.

---

## ▶️ How to Run

1. Open the project in **PyCharm**.
2. Make sure Python is configured correctly.
3. Install the required libraries.
4. Open any Python file.
5. Click **Run** in PyCharm.

For example:

```bash
python image_read.py
```

---

## 🧠 What I Learned

Through this project, I learned the basic workflow of OpenCV:


Image / Video / Webcam
        ↓
     Read Data
        ↓
  Process the Data
        ↓
 Apply OpenCV Operations
        ↓
 Display / Save Result


I also gained practical understanding of:

* Image representation
* Image dimensions and aspect ratio
* Image transformations
* Image filtering
* Noise reduction
* Thresholding
* Edge detection
* Video processing
* Real-time webcam processing

---

## 🚀 Future Learning

I plan to explore more advanced Computer Vision concepts such as:

* Face Detection
* Face Recognition
* Object Detection
* Contour Detection
* Image Segmentation
* Feature Detection
* Motion Detection
* Real-time Object Tracking
* OpenCV with Machine Learning
* OpenCV with Deep Learning

---

## 👨‍💻 Author

**Tanuj Deepak Tambe**

Learning **Python, OpenCV, Computer Vision and AI/ML**.

---

## ⭐ Purpose

This repository is mainly created for **learning, practicing, and documenting my progress in OpenCV with Python**.
