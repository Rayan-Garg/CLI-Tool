import fire
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image
import os

#setting up video information
source_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, 'audio.mp3')
clip = VideoFileClip(source_path)
duration = clip.duration
fps = clip.reader.fps
nframes = clip.reader.nframes
w,h = clip.size

def make_thumbnail(frame_num=1):
    if frame_num is None:
        print("Default frame 1 being used to create thumbnail, due to no frame number provided")
    if frame_num in range(0,int(duration)+1):
        thumbnail_dir = os.path.join(SAMPLE_OUTPUTS,"thumbnails")
        os.makedirs(thumbnail_dir,exist_ok=True)
        frame = clip.get_frame(int(frame_num))
        new_img_filepath = os.path.join(thumbnail_dir, f"Thumbnail (Frame {frame_num}).jpg")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)
    else:
        print("Not a valid frame for inputted video. Try again")

def create_video():
    print("creating video from images in input directory")
    images_dir = os.path.join(SAMPLE_INPUTS,"images")
    output_path = os.path.join(SAMPLE_OUTPUTS,'created_video.mp4')
    directory = {}
    for root, dirs, files in os.walk(images_dir):
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
    clip.write_videofile(output_path)

def create_gif(start_sec=10, end_sec=20):
    #can create a gif from a user decided subclip of the input video
    GIF_DIR = os.path.join(SAMPLE_OUTPUTS,'gifs')
    os.makedirs(GIF_DIR,exist_ok=True)
    output_path1 = os.path.join(GIF_DIR,'usergif.gif')
    if start_sec in range(0,int(duration)+1) and end_sec in range(0,int(duration)+1):
        subclip = clip.subclip(start_sec,end_sec)
        subclip = subclip.resize(width=500)
        subclip.write_gif(output_path1,fps=20,program="ffmpeg")

def combine_audios():
    mix_audio_dir = os.path.join(SAMPLE_OUTPUTS,"mixed-audio")
    os.makedirs(mix_audio_dir,exist_ok=True)
    og_audio_path = os.path.join(mix_audio_dir, 'og.mp3')
    final_audio_path = os.path.join(mix_audio_dir, 'final-audio.mp3')     
    final_video_path = os.path.join(mix_audio_dir, 'final-video.mp4')  
    
    original_audio = clip.audio
    original_audio.write_audiofile(og_audio_path)

    background_audio_clip = AudioFileClip(source_audio_path)
    bg_music = background_audio_clip.subclip(0,clip.duration)

    final_audio = CompositeAudioClip([original_audio,bg_music])
    final_audio.write_audiofile(final_audio_path,fps=original_audio.fps)

    final_clip = clip.set_audio(final_audio)
    final_clip.write_videofile(final_video_path)

def add_watermark(watermark_value="watermark", watermark_size=60):
    if watermark_value is None or watermark_size is None:
        print("Using default value because watermark size or text was not provided")
    watermark_text = TextClip(watermark_value,fontsize=watermark_size,color='white',align='West',size=(w,watermark_size))
    watermark_text = watermark_text.set_fps(fps)
    watermark_text = watermark_text.set_duration(duration)
    watermark_text = watermark_text.margin(left = 10,right = 10,bottom=2,opacity=0)
    watermark_text = watermark_text.set_position(("bottom"))

    overlay_clip = CompositeVideoClip([clip,watermark_text],size=clip.size)
    overlay_clip = overlay_clip.set_duration(duration)
    overlay_clip = overlay_clip.set_fps(fps)
    overlay_clip = overlay_clip.set_audio(AudioFileClip(source_audio_path))
    output_path2 = os.path.join(SAMPLE_OUTPUTS,'video_with_watermark.mp4')
    overlay_clip.write_videofile(output_path2)

class Pipeline(object):
    def __init__(self):
        self.thumbnail = make_thumbnail
        self.create_video = create_video
        self.create_gif = create_gif
        self.combine_audios = combine_audios
        self.add_watermark = add_watermark
        
if __name__ == '__main__':
    fire.Fire(Pipeline)
