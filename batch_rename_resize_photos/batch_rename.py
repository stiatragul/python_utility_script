from PIL import Image
import PIL
import os
import glob

# Multiple images in current directory 
directory_files = os.listdir()

# List and print all images (ending with .jpg, .JPG, .png, etc)
multiple_images = [file for file in directory_files if file.endswith(('.jpg', '.JPG', '.png'))]
print(multiple_images)

# # Resize image based on width. For my web I want 2000 px
base_width = 2500

# # # Loop over each image
# for image in multiple_images:
    img = Image.open(image)
    width_percent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(width_percent)))
    img = img.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    #preserve metadata
    img.save('resized_'+image, optimize=True, quality=70)