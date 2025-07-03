# Real-Time Object Detection

This project demonstrates real-time object detection using the YOLO (You Only Look Once) model. It supports both **image** and **video** input, drawing bounding boxes around detected objects with their class labels and confidence scores.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Sample Output](#sample-output)
- [License](#license)

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/ShyamSanjeyS/Object-Detection-Iamge-video.git
   cd Real-Time-Object-Detection-Iamge-Video
   ```

   [🔗 GitHub Repo Link](https://github.com/ShyamSanjeyS/Real-Time-Object-Detection-Iamge-Video)

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input files inside the `data/` folder:
   - Image file (e.g., `img1.jpg`)
   - Video file (e.g., `video1.mp4`)
   - Class labels file (`classes.txt`)

2. Run the main script:

   ```bash
   python main.py
   ```

3. Choose the input type when prompted:
   - Type `image` for image detection
   - Type `video` for video detection

4. Output behavior:
   - For **images**: A window will display the results. Press any key to close.
   - For **videos**: The detection will play frame by frame. Press `q` to quit.

## Project Structure

```
Real-Time-Object-Detection/
│
├── data/
│   ├── img1.jpg
│   ├── video1.mp4
│   ├── classes.txt
│   └── yolo-Weights/
│       └── yolov8n.pt
│
├── output/
│   ├── output_image.png
│   └── output_video.png
│
├── src/
│   ├── __init__.py
│   ├── object_detection_image.py
│   ├── object_detection_video.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── main.py
```

- `data/`: Input images, videos, model weights, and class label files.
- `src/`: Core logic for object detection (image/video) and utilities.
- `main.py`: Entry point to run the project.
- `output/`: Stores output results (images/frames).
- `requirements.txt`: Lists all dependencies.

## Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python`)
- Ultralytics (`ultralytics`)

Install all packages using:

```bash
pip install -r requirements.txt
```

## Sample Output

### 🔹 Image Detection Output

![Image Detection Output](output/output_image.png)

---

### 🔹 Video Detection (Sample Frame)

![Video Detection Frame](output/output_video.png)

## License

This project is licensed under the [MIT License](LICENSE).
