import cv2
import os


def extract_frames(vid_path: str, frame_dir: str) -> None:
    cam = cv2.VideoCapture(vid_path)

    try:
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

    except OSError:
        print('Error: Creating directory of data')

    currentframe = 1

    while True:
        ret, frame = cam.read()
        if ret:
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    extract_frames('Cow Rumination 2.mp4', './data/extracted_frames')
