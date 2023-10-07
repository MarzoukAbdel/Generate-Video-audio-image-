from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text):
    # Load the image
    image = Image.open(image_path)

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Define the font style and size
    font = ImageFont.truetype('D:/augenratePy/OLDENGL.TTF', 150)  # You can change the font and size here

    newsize=(1920,1080)
    image = image.resize(newsize)
    # Get the size of the image
    image_width, image_height = image.size


    # Get the size of the text
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position to center the text
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2 )-120
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



#image_path = 'D:/augenratePy/image/pexels-bobby-nguyen-9649595.jpg'   # Path to your input image
#text = 'HMED'  # The text you want to add
#output_path = 'D:/augenratePy/output/output_image.jpg'   # Path to save the output image

#my_image=add_text_to_image(image_path, text)

