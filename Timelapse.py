import imageio
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import cv2
import time

''' I am having a problem where when the videos is played back the images are
    not a constant frame rate'''

save_folder = 'processed\\'
photo_folder = 'C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Pictures\\2024\\Italy\\torino-park-timelapse\\'
#'C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Pictures\\2024\\plant-evolution\\'
fps = 35


def get_image_dirs():
    # Get the directories of the images
    image_dirs = []
    for root, dirs, files in os.walk(photo_folder):
        for f in files:
            if (f.endswith('.JPG') or f.endswith('.jpg')):
                image_dirs.append(os.path.join(root, f))
    return image_dirs



# def stitch_images():
#     images = get_image_dirs()
#     writer = imageio.get_writer(save_folder + f'timepalse_{datetime.now().strftime("%Y%m%d_%H%M%S")}.mp4', 
#                                 fps=fps)
#     for i in tqdm(range(len(images))):
#         ## Load the image
#         image = imageio.v2.imread(images[i])
#         writer.append_data(image)
#         # writer.append_data(frame_uint8)
#     print('Saving video...')
#     writer.close()


def stitch_images():
    images = {'image': get_image_dirs(), 'time': []}
    ## I have to do this because the names of the image names are not in order ##
    for dir in images['image']:
        images['time'].append(time.ctime(os.path.getctime(dir)))

    images_df = pd.DataFrame(images)
    images_df = images_df.sort_values('time', ascending=True).reset_index(drop=True)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    writer = cv2.VideoWriter(save_folder+f'timelapse_{datetime.now().strftime("%Y%m%d_%H%M%S")}.mp4', 
                             fourcc, 30, (6000,4000)) #cv2.VideoWriter_fourcc(*"MP4V"), 0x7634706d
    print(len(images_df))
    print('Writing video...')
    for i in tqdm(range(len(images['image']))): 
        writer.write(cv2.imread(images_df['image'].iloc[i]))
    writer.release()


def main():
    ## run the timelapse ##
    # stitch_videos()
    stitch_images()
    ## add more editing things here later ##

if __name__ == '__main__':
    main()
