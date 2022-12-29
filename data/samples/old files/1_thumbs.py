from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
import os

source_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS,"thumbnails")
os.makedirs(thumbnail_dir,exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)
duration = clip.duration
fps = clip.reader.fps
nframes = clip.reader.nframes
for i in range(0,int(duration)+1):
    print(f"frame at {i} seconds")
    frame = clip.get_frame(int(i))
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)