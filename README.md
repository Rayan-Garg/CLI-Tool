# CLI-Tool

This is a CLI Tool created with Python, the MoviePy library, and the Fire library, that can take in specific commands to then edit videos. 

<h1>Setup</h1>
Run the following in the command line: <br/>
<space><space>*<space> brew update && brew install ffmpeg <br/>
<space><space>*<space> pip install fire <br/>
<br/>
The input video, images, and audio used by the tool are in the inputs folder, and the user can change any of these inputs to their own preference 

<h1>Details</h1>
The tool has 5 commands that can be called from the terminal: <br/>
1. thumbnail - makes a thumbnail from a selected image <br/>
    Takes one integer argument(frame_num) indicating which frame of the video to turn into the thumbnail. The default value is 1. <br/>
2. create_video - creates a video from a set of images in the inputs directory <br/>
3. create_gif - creates a gif from a subclip of the video <br/>
    Takes two integer arguments(start_sec, end_sec) to decide which part of video is clipped <br/>
4. combine_audios - takes 2 audios from input directory and overlays them to create a video with combined audios <br/>
5. add_watermark - adds a watermark to the input video <br/>
    Takes two arguments(watermark_text(string),watermark_size(integer)) in corresponding order. Both have default values and can be referred to as named arguments <br/>
