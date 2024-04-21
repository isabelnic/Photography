import imageio
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

root_folder = 'C:\\Users\\hanna\\OneDrive - University of Edinburgh\\Desktop\\Photography-code\\Photography\\to-process\\'



def get_image_dirs():
    # Get the directories of the images
    image_dirs = []
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            if (f.endswith('.JPG') or f.endswith('.jpg')):
                image_dirs.append(os.path.join(root, f))
    return image_dirs



def stitch_videos():
    images = get_image_dirs()
    writer = imageio.get_writer(root_folder + f'timepalse_{datetime.now().strftime("%Y%m%d_%H%M%S")}.mp4', 
                                fps=20)
    for i in tqdm(range(len(images))):
        ## Load the image
        image = imageio.v2.imread(images[i])
        writer.append_data(image)
        # writer.append_data(frame_uint8)
    print('Saving video...')
    writer.close()


def main():
    ## run the timelapse ##
    stitch_videos()


if __name__ == '__main__':
    main()
