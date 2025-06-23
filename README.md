

---

````markdown
# Car Detection in Video Sequences using Gaussian Mixture Models (GMM) - MATLAB

This project implements car detection in video sequences using **Gaussian Mixture Models (GMM)** for background subtraction, **morphological operations** for noise removal, and **blob analysis** for object tracking.

The system detects moving vehicles in a video, draws bounding boxes around each detected car, and displays the number of detected cars per frame.

---

## Project Workflow

### 1. Video Input and Initialization

- Load the input video using `VideoReader`.
- Initialize a foreground detector (`vision.ForegroundDetector`) with 8 Gaussian modes and a training period of 50 frames.

### 2. Foreground Detection and Processing

- Apply GMM-based background subtraction to detect foreground objects.
- Perform morphological opening (`imopen`) using a square structural element to reduce noise.
- Detect connected components using `vision.BlobAnalysis`.

### 3. Visualization and Output

- Draw bounding boxes around detected cars using `insertShape`.
- Display the number of cars in each frame using `insertText`.
- Use `vision.VideoPlayer` to show the processed video in real-time.

---

## Code Explanation

### Foreground Detector Initialization

```matlab
foregroundDetector = vision.ForegroundDetector('NumGaussians', 8, 'NumTrainingFrames', 50);
````

* Initializes the GMM-based foreground detector.

### Reading the Video

```matlab
videoReader = VideoReader('/MATLAB Drive/Examples/R2024a/vision/car.mp4');
```

* Reads frames from the input video.

### Training Phase

```matlab
for i = 1:150
    frame = readFrame(videoReader);
    foreground = step(foregroundDetector, frame);
end
```

* Uses 150 frames to train the background model.

### Foreground Extraction and Noise Removal

```matlab
se = strel('square', 7);
filteredForeground = imopen(foreground, se);
```

* Applies morphological opening to clean the foreground mask.

### Blob Analysis

```matlab
blobAnalysis = vision.BlobAnalysis('BoundingBoxOutputPort', true, 'MinimumBlobArea', 1000);
bbox = step(blobAnalysis, filteredForeground);
```

* Detects connected components corresponding to moving vehicles.

### Drawing Bounding Boxes and Car Count

```matlab
result = insertShape(frame, 'Rectangle', bbox, 'ShapeColor', 'green');
numCars = size(bbox, 1);
result = insertText(result, [10 10], numCars, 'BoxOpacity', 1, 'FontSize', 14);
```

* Overlays bounding boxes and car count on the frame.

### Real-time Processing Loop

```matlab
while hasFrame(videoReader)
    frame = readFrame(videoReader);
    foreground = step(foregroundDetector, frame);
    filteredForeground = imopen(foreground, se);
    bbox = step(blobAnalysis, filteredForeground);
    result = insertShape(frame, 'Rectangle', bbox, 'ShapeColor', 'green');
    numCars = size(bbox, 1);
    result = insertText(result, [10 10], numCars, 'BoxOpacity', 1, 'FontSize', 14);
    step(videoPlayer, result);
end
```

* Processes each frame and displays results in real-time.

---

## How to Run

1. Open MATLAB (R2024a or compatible version).
2. Make sure the required toolbox is installed:

   * Computer Vision Toolbox
3. Place your video file in your working directory (or adjust the path in the code).
4. Run the main script in MATLAB.

---

## Dependencies

* MATLAB R2024a or compatible version
* Computer Vision Toolbox

---

## Example Output
![image](https://github.com/user-attachments/assets/b04fbcd1-23a9-46a6-a17c-6ddd4ca78780)


---

## License

This project is for academic and educational use only.

---

## Contact

For any questions, please contact:

**Akanksha Bhagat**
Email: [akankshabhagat2127@gmail.com](mailto:akankshabhagat2127@gmail.com)
LinkedIn: [linkedin.com/in/akanksha-bhagat](https://linkedin.com/in/akanksha-bhagat)

---


