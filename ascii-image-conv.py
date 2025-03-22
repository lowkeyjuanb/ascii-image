# IMPORTS
from PIL import Image


# 30 levels of gray using ASCII
ascii_values = '░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓'   

image_name = str(input("Enter the name of the image: "))
# Opening image and converting it to grayscale.
image = Image.open(str(image_name)).convert('L')

# Input for the new width of the image.
new_width = int(input("Select the width for the image: "))

# Height is calculated and adjusted to preserve the aspect ratio
new_height = int(((image.height * new_width) / image.width) *.5) 

# Resizing the image.
image = image.resize((new_width, new_height))
print("Image size", image.size) # New image size

# Get pixel values
pixels = image.getdata()

# Goes from 0 to 255 typically since it is based in rgb
print("Min value - " + str(min(pixels))) 
print("Max value - " + str(max(pixels))) 

# Array to join each row of pixels from the image.
full_image = []
row = []
counter = 0
width, height = image.size  # Get width and height of the image

# Map grayscale pixels to ASCII characters
for pixel in pixels:
    if counter == width:  # If counter reaches the width, print and reset row
        full_image.append("".join(row))
        row.clear()  # Clear the row for the next line
        counter = 0  # Reset counter for the next row
    
    # Map pixel to an ASCII character
    row.append(ascii_values[int(pixel/8.5)])
    counter += 1

full_image = "\n".join(full_image)

with open("ascii-image.txt", "w") as f:
    f.write(str(full_image))