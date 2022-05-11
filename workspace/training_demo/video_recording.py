import numpy as np
import cv2
import os
import uuid


def get_images_and_videos(IMAGE_PATH, VIDEO_PATH, mood, time=5):  # time in minutes
    video_final_path = os.path.join(VIDEO_PATH, mood, str(uuid.uuid1()) + ".avi")
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_final_path, fourcc, 30.0, (640, 480))
    total_frames = 30 * time * 60 + 30
    count = 0
    while True:
        if count < 30:
            count += 1
            continue
        ret, frame = cap.read()
        if count % 60 == 0:
            image_final_path = os.path.join(IMAGE_PATH, str(uuid.uuid1()) + ".jpg")
            cv2.imwrite(image_final_path, frame)
        count += 1
        out.write(frame)
        cv2.imshow('Original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count == total_frames:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def main():
    IMAGE_PATH = "raw_data/images/"
    VIDEO_PATH = "raw_data/videos/"

    while True:
        print()
        print("#######################################################################")
        print("##                                                                   ##")
        print("##   Welcome to video recording session for Mood Detection Project   ##")
        print("##                                                                   ##")
        print("#######################################################################")
        print()
        print()
        print("Choose an option : ")
        print("1. Active")
        print("2. Drowsy")
        print("3. Exit")
        n = int(input("Choose an option : "))
        if n == 1:
            get_images_and_videos(IMAGE_PATH, VIDEO_PATH, "active", 5)
        elif n == 2:
            get_images_and_videos(IMAGE_PATH, VIDEO_PATH, "drowsy", 5)
        elif n == 3:
            break
        else:
            continue


main()
