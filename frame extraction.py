import json
import os
import cv2


def create_count_file(path):
    """Creates a JSON file at the specified path with a 'count' key initialized to 0.

    Args:
      path: The path to the JSON file.
    """
    if not os.path.exists(path):
        data = {'count': 0}
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)


def read_count(path):
    """Reads the 'count' value from the JSON file at the specified path.

    Args:
      path: The path to the JSON file.

    Returns:
      The 'count' value from the JSON file.
    """
    with open(path, 'r') as f:
        data = json.load(f)
        return data['count']


def update_count(path, new_count):
    """Updates the 'count' value in the JSON file at the specified path.

    Args:
      path: The path to the JSON file.
      new_count: The new value for the 'count' key.
    """
    data = {'count': new_count}
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def extract_frames(vid_path: str, frame_dir: str) -> None:
    """
        Extracts frames from the given video file and saves them to a directory.

        Parameters:
        vid_path (str): The path to the video file.
        frame_dir (str): The directory where the extracted frames will be stored.

        Creates the directory if it does not exist and writes frames as JPEG files.
        """
    cam = cv2.VideoCapture(vid_path)

    try:
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

    except OSError:
        print('Error: Creating directory of data')
    path = 'count.json'

    # Create the file if it doesn't exist
    create_count_file(path)
    # Read the current count
    count = read_count(path)

    currentframe = count

    while True:
        ret, frame = cam.read()
        if ret:
            name = os.path.join(frame_dir, f'frame{currentframe}.jpg')
            print('Creating...' + name)

            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    update_count(path, currentframe)

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    for file in os.listdir('samples'):
        extract_frames(f'samples/{file}', 'data/extracted_frames')
    # extract_frames('samples/Rumination 3.mp4', 'data/extracted_frames')
