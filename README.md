
🚗 Car Detection in Video Sequences using Gaussian Mixture Models (GMM)
This project demonstrates the use of Gaussian Mixture Models (GMM) for detecting moving vehicles in video sequences. The model leverages background subtraction techniques to identify foreground objects (cars), followed by noise removal and object tracking.

🔍 Project Workflow
Video Input & Initialization

Load video sequences.

Initialize training for n Gaussian modes in the mixture model.

Foreground Detection & Processing

Perform background subtraction using GMM.

Apply morphological opening to reduce noise.

Use blob analysis to detect and track car-like objects.

Visualization & Output

Display bounding boxes around detected cars in each frame.

Count and display the number of cars detected per frame.

Generate a processed video stream with overlays.

🛠️ Techniques Used
Gaussian Mixture Models (GMM) for background subtraction

Morphological transformations (Opening)

Blob detection and analysis

Object tracking across frames

