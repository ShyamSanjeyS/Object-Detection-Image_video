from src import object_detection_image, object_detection_video

def main():
    mode = input("Enter mode (image/video): ").strip().lower()

    if mode == "image":
        object_detection_image.main()
    elif mode == "video":
        object_detection_video.main()
    else:
        print("Invalid mode. Please enter 'image' or 'video'.")

if __name__ == "__main__":
    main()
