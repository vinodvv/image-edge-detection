# Edge Detection with OpenCV

This project demonstrates a simple implementation of edge detection using the Canny Edge Detection algorithm in OpenCV and Python.

## Getting Started

1. Prerequisites:

   * Python 3.x
   * OpenCV (install using pip install opencv-python)
   * Matplotlib (install using pip install matplotlib)

   
2. Run the script:

    * Replace "images/image_3.jpeg" in the code with the path to your image.
    * Run the script using python edge_detection.py (assuming your script is named edge_detection.py).

## The Script

The script performs the following steps:

1. Loads the image in grayscale mode.
2. Applies Gaussian Blur to reduce noise.
3. Performs Canny Edge Detection to detect edges in the image.
4. Visualizes the results by displaying the original and edge-detected images side-by-side.
5. Optionally saves the edge-detected image as a new file.

## Explanation:

The code includes comments to explain each step.

## Further Exploration:

* Experiment with different threshold values in the cv2.Canny() function to see how they affect the edge detection results.
* Explore other image processing techniques available in OpenCV.