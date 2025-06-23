# Car Detection in Video Sequences using Gaussian Mixture Models (GMM) - MATLAB

This project implements car detection in video sequences using Gaussian Mixture Models (GMM) for background subtraction, morphological operations for noise removal, and blob analysis for object tracking.

The system detects moving vehicles in a video, draws bounding boxes around each detected car, and displays the number of detected cars per frame.

---

## Project Workflow

### 1. Video Input and Initialization

The system begins by reading video frames using MATLAB’s built-in video reader.  
A foreground detector based on Gaussian Mixture Models (GMM) is initialized to model the background.  
The detector is trained on an initial set of frames to learn the background and distinguish between static and moving objects.

---

### 2. Foreground Detection and Processing

For each frame, background subtraction is performed using the trained GMM detector to extract a foreground mask of moving objects.  
Morphological operations (such as opening) are applied to the mask to reduce noise and remove small irrelevant objects.

---

### 3. Object Detection (Blob Analysis)

After noise reduction, blob analysis is performed to identify connected components in the foreground mask that correspond to moving vehicles.  
Blobs that meet a minimum size threshold are classified as valid car detections.

---

### 4. Visualization and Output

Bounding boxes are drawn around each detected car in the video frame.  
The system also counts the number of detected cars and overlays this information on the video.  
The processed video is displayed in real time using a video player.

---

## Summary

This project demonstrates a classical computer vision approach for vehicle detection in video sequences using:
- Gaussian Mixture Models (GMM) for background subtraction
- Morphological filtering for noise reduction
- Blob analysis for object detection and tracking

---

## How to Run

1. Open MATLAB (R2024a or compatible version).
2. Make sure the required toolbox is installed:
   - Computer Vision Toolbox
3. Place your video file in your working directory (or adjust the path in the code).
4. Run the main script in MATLAB.

---

## Dependencies

- MATLAB R2024a or compatible version
- Computer Vision Toolbox

---

## Example Output

(Add an image here showing detected cars with bounding boxes.)

---

## License

This project is for academic and educational use only.

---

## Contact

For any questions, please contact:

**Akanksha Bhagat**  
Email: [akankshabhagat2127@gmail.com](mailto:akankshabhagat2127@gmail.com)  
LinkedIn: [linkedin.com/in/akanksha-bhagat](https://linkedin.com/in/akanksha-bhagat)

