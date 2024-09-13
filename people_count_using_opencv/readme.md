# People Counting using OpenCV

This project demonstrates how to count the number of people in a video stream or images using OpenCV and a pre-trained deep learning model (e.g., MobileNet SSD or YOLO). The system can detect and count people in real-time from a webcam feed or from video and image files.

## Features

- **Real-time People Counting**: Detects and counts people in real-time using a webcam.
- **Video Processing**: Detects and counts people in video files.
- **Image Processing**: Detects and counts people in static images.
- **Scalability**: Can be extended to count other objects using different models.
- **Cross-platform**: Can run on any platform where OpenCV is supported.

## Prerequisites

Before you begin, ensure you have the following software and libraries installed:

- Python 3.x
- OpenCV
- Pre-trained model (MobileNet SSD, YOLO, etc.)
- `numpy`
- `imutils`

### Installing Required Libraries

You can install the required Python libraries using pip:

```bash
pip install numpy opencv-python imutils
