from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os
import random


def add_text_to_image(image_path, text):
    # Load the image
    image = Image.open(image_path)

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Define the font style and size
    font = ImageFont.truetype('D:/augenratePy/OLDENGL.TTF', 150)  # You can change the font and size here


    # Get the size of the image
    image_width, image_height = image.size


    # Get the size of the text
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position to center the text
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    #position = (960, 540)

    # Define the text color
    text_color = (255, 255, 255)  # White color
    text_color = (255, 255, 255)  # White color
    shadow_color = (0, 0, 0, 100)

    # Add the text to the image

    shadow_offset = 7  # Adjust the shadow offset as needed
    shadow_position = (position[0] + shadow_offset, position[1] + shadow_offset)
    draw.text(shadow_position, text, font=font, fill=shadow_color)
    draw.text(position, text, font=font, fill=text_color)

    # Save the modified image
    image.save(image_path)
    return image_path;

# Set the paths for the audio file and image
audio_folder_path  = "D:/augenratePy/audio"
image_folder_path  = "D:/augenratePy/image"
# Load the audio file using moviepy's AudioFileClip class

audio_files = [f for f in os.listdir(audio_folder_path) if os.path.isfile(os.path.join(audio_folder_path, f))]
image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

# Set the output video filename prefix
output_prefix = "output_"
# Choose a filename for the output video
output_dir = "D:/augenratePy/output"


# Loop to create multiple videos
for i in range(1): # Change the value in range to specify how many videos to create
    # Randomly select an audio file and an image file
    audio_file = os.path.join(audio_folder_path, random.choice(audio_files))
    image_file = add_text_to_image(os.path.join(image_folder_path, random.choice(image_files)),"MAFZ")

    # Set the output video filename
    output_filename = output_prefix + str(i) + ".mp4"
    output_path = os.path.join(output_dir, output_filename)
 # Load the audio file and image file
    audio_clip = AudioFileClip(audio_file)
    image_clip = ImageClip(image_file)
    #size
    newsize=(1920,1080)
    image_sized = image_clip.resize(newsize)
    # Set the duration of the video to be the same as the duration of the audio clip
    video_clip = image_sized.set_duration(audio_clip.duration)
    final_clip = video_clip.set_audio(audio_clip)
# Write the final clip to a video file
    final_clip.write_videofile(output_path, fps=20)
