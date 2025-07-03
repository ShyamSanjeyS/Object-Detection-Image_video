import cv2
import numpy as np
from ultralytics import YOLO
from .utils import read_class_names

# Constants
image_file_path = "data/img1.jpg"
yolo_weights_path = "data/yolo-Weights/yolov8n.pt"
class_names_file = "data/classes.txt"

def main():
    # Read the image
    frame = cv2.imread(image_file_path)
    if frame is None:
        print("Error: Could not read image file.")
        return

    # Resize image to medium size (optional: adjust as needed)
    frame = cv2.resize(frame, (800, 600))  # width=800, height=600

    # Load YOLO model and class names
    model = YOLO(yolo_weights_path)
    class_names = read_class_names(class_names_file)

    # Perform object detection
    results = model(frame)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Display confidence and class name
            confidence = np.round(box.conf[0], decimals=2)
            cls = int(box.cls[0])
            class_name = class_names[cls]

            text = f"{class_name}: {confidence:.2f}"
            org = (x1, y1 - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            color = (0, 255, 0)
            thickness = 1

            cv2.putText(frame, text, org, font, font_scale, color, thickness)

    # Set up a resizable window and resize it
    cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Object Detection', 800, 600)

    # Display the image
    cv2.imshow('Object Detection', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
