import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all import crop


source_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS,'gifs')
os.makedirs(GIF_DIR,exist_ok=True)
output_path1 = os.path.join(GIF_DIR,'sample1.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10,20)
subclip = subclip.resize(width=500)
subclip.write_gif(output_path1,fps=20,program="ffmpeg")

