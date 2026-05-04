# Car Detection in Video Sequences using Gaussian Mixture Models

Real-time vehicle detection, counting, and motion analysis in traffic video using **GMM-based foreground detection** combined with **Lucas-Kanade optical flow** — implemented in MATLAB.

---

## Overview

Urban traffic congestion is a critical challenge for city infrastructure management. Traditional monitoring methods fail to capture dynamic traffic patterns accurately. This project builds a computer vision pipeline that detects and counts moving vehicles in video sequences in real time, using statistical background modeling and optical flow analysis.

---

## Demo

> Green bounding boxes drawn around detected vehicles in each frame with a live vehicle count overlay.

*(See `car.mp4` for sample output)*

---

## Pipeline

```
Video Input (MP4/AVI)
        ↓
Frame Extraction (VideoReader)
        ↓
GMM Foreground Detection
  └── NumGaussians: 8
  └── NumTrainingFrames: 50
        ↓
Morphological Opening (noise removal)
        ↓
Blob Analysis (min area: 1000px)
  └── Bounding box extraction
        ↓
Vehicle Count Overlay + Bounding Box Display
        ↓
Lucas-Kanade Optical Flow (ROI-masked)
  └── Vehicle velocity & direction estimation
        ↓
Real-time Video Output
```

---

## Methodology

### 1. GMM-Based Foreground Detection
- Initialized a Gaussian Mixture Model foreground detector with `NumGaussians=8` and `NumTrainingFrames=50`
- The model learns the static background during the training phase
- Tuned GMM parameters separately for light traffic and heavy traffic videos to improve detection accuracy

### 2. Morphological Processing
- Applied morphological opening to the foreground mask to remove small noise artifacts
- Improves region quality before blob analysis

### 3. Blob Analysis
- Extracted connected components (blobs) from the filtered foreground mask
- Computed bounding boxes around each detected vehicle blob
- Minimum blob area threshold of 1000px to filter out false positives

### 4. Lucas-Kanade Optical Flow
- Computed dense optical flow vectors within defined Regions of Interest (ROIs) focused on road areas
- ROI masking isolates vehicle motion from background noise
- Optical flow arrows overlaid on frames show vehicle direction and speed
- Frame rate adjusted for controlled visual inspection of motion

---

## Dataset

- **Primary:** `car.mp4` — standard traffic test video
- **Additional:** 2 YouTube traffic videos (light traffic + heavy traffic) in MP4 and AVI formats

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | MATLAB |
| Video I/O | VideoReader, VideoPlayer |
| Detection | Gaussian Mixture Model (GMM) |
| Tracking | Blob Analysis, Lucas-Kanade Optical Flow |
| Processing | Morphological Opening |

---

## Results

- Vehicles detected and counted frame-by-frame in real time
- Green bounding rectangles drawn around each detected vehicle
- Vehicle count displayed as overlay on each frame
- Optical flow vectors show vehicle velocity and direction within ROIs
- System tested on both light and heavy traffic scenarios with parameter tuning

---

## Project Structure

```
├── car.mp4                        # Sample test video
├── car_detection_gmm.m            # Main MATLAB script — GMM detection + blob analysis
├── optical_flow_lk.m              # Lucas-Kanade optical flow analysis
├── CarDetectionG.pptx             # Project presentation
└── README.md
```

---

## How to Run

1. Open MATLAB
2. Place your video file in the working directory (or update the path in the script)
3. Run `car_detection_gmm.m` for vehicle detection and counting
4. Run `optical_flow_lk.m` for optical flow analysis

**Key parameters to tune based on your video:**
```matlab
foregroundDetector = vision.ForegroundDetector(
    'NumGaussians', 8,           % Increase for complex backgrounds
    'NumTrainingFrames', 50      % Frames used to learn background
);
blobAnalyzer.MinimumBlobArea = 1000;  % Adjust for vehicle size in frame
```

---

## Authors

- **Akanksha Vikram Bhagat** (23MAI1007)
- Oriana Gabriella Manners (23MAI1014)

**Institution:** School of Computer Science & Engineering, Vellore Institute of Technology, Chennai
**Course:** Machine Vision — Prof. Dr. G. Malathi, SCOPE

---

## Future Work

- Port implementation to Python (OpenCV) for broader accessibility
- Add vehicle classification (car vs truck vs bike)
- Integrate with live CCTV feed for real-time traffic monitoring
- Use deep learning-based detectors (YOLO) for comparison
