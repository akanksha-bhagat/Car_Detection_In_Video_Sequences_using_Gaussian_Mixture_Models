#Here's Equivalent Python code for My Matlab's Computer Vison's version
import cv2
import numpy as np

# Initialize video reader
video_path = 'car.mp4'  # your video file path
cap = cv2.VideoCapture(video_path)

# Create background subtractor (GMM)
foreground_detector = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=100, detectShadows=True)

# Structuring element for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# Process first 150 frames for training
for i in range(150):
    ret, frame = cap.read()
    if not ret:
        break
    foreground = foreground_detector.apply(frame)

# Display one frame and its foreground mask
cv2.imshow('Video Frame', frame)
cv2.imshow('Foreground', foreground)
cv2.waitKey(0)

# Morphological opening to reduce noise
filtered_foreground = cv2.morphologyEx(foreground, cv2.MORPH_OPEN, kernel)
cv2.imshow('Clean Foreground', filtered_foreground)
cv2.waitKey(0)

# Reinitialize video for full processing
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Create video writer to save output (optional)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('detected_cars.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Process the video
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect foreground
    foreground = foreground_detector.apply(frame)
    
    # Morphological opening to reduce noise
    filtered_foreground = cv2.morphologyEx(foreground, cv2.MORPH_OPEN, kernel)
    
    # Find contours (blob analysis)
    contours, _ = cv2.findContours(filtered_foreground, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    num_cars = 0
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Minimum blob area
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            num_cars += 1
    
    # Insert number of detected cars
    cv2.putText(frame, f'Cars detected: {num_cars}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 0, 255), 2)
    
    # Show result
    cv2.imshow('Detected Cars', frame)
    
    # Save frame to output video
    output.write(frame)
    
    # Exit on ESC key
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release resources
cap.release()
output.release()
cv2.destroyAllWindows()
