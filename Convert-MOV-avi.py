import cv2
import imageio
import numpy as np
import os

video_dir = "C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Desktop\\Photography-code\\Photography\\processed\\timepalse_20240421_124045.mp4"
timelapsefps = 10 # false is not timelapse, number for timelapse new framerate
photo_folder = 'C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Pictures\\2024\\plant-evolution\\'
#'C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Pictures\\2024\\Italy\\milan-timelapse\\'
#
 

def find_files_with_name(root_folder, filename):
    found_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if (file == filename) or (filename in file):
                found_files.append(os.path.join(root, file))
    return found_files


def read_video(dir):
    cap = cv2.VideoCapture(dir)
    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # start reading from the start_frame
    ret = True
    while ret: # read all frames
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame.")
            break
        frames.append(frame)

    # Release the video capture object
    cap.release()
    return frames


def read_photos(folder):
    dirs = find_files_with_name(folder, '.JPG')
    frames = []
    for d in dirs:
        img = imageio.imread(d, pilmode='RGB')
        frames.append(img)
    return frames


def save_video(frames, dir):
    filename = dir.split('\\')[-1].split('.')[0]
    folder = '\\'.join(dir.split('\\')[0:-1])
    if timelapsefps == False: fps=30
    else: fps = timelapsefps
    writer = imageio.get_writer(folder + '\\' + filename + f'_{fps}.avi', fps=fps)  # fps=
    for frame in frames: # Iterate through the frames and add them to the video
        # Ensure the frame data type is uint8 for imageio
        frame_uint8 = (frame).astype(np.uint8)
        writer.append_data(frame_uint8)
    writer.close()


def main(dir):
    if timelapsefps == False:
        frames = read_video(dir)
        save_video(frames, dir)
    else:
        frames = read_photos(photo_folder)
        save_video(frames, photo_folder + 'timelapse.avi')
    


main(video_dir)