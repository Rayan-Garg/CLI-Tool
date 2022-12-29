from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
import os

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS,"thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS,"thumbnails-per-frame")
thumbnail_per_half_second = os.path.join(SAMPLE_OUTPUTS,"thumbnails-per-half-second")
output_video = os.path.join(SAMPLE_OUTPUTS,'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, file) for file in this_dir if file.endswith("jpg")]

directory = {}
for root, dirs, files in os.walk(thumbnail_dir):
    for _files in files:
        filepath = os.path.join(root,_files)
        try:
            key = float(_files.replace(".jpg",""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    new_paths.append(directory[k])

clip = ImageSequenceClip(new_paths,fps=1)
clip.write_videofile(output_video)

frame = ImageClip(new_paths[1])
print(dir(frame))
#can iterate through a for loop and ImageClip each path to a frame. Call dir on the frame to see what you can call. 