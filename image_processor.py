import time
from PIL import Image 

# Step-1: FIrst generate the number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print("Random Generated Number:", generated_number)

# Step-2: Open the image (chapter1.jpg) from the directory and modify the pixel values
image = Image.open('./chapter1.jpg')  
pixels = image.load()  # It Load pixel data

width, height = image.size
new_image = Image.new("RGB", (width, height))  # Create a new image with the same size

total_red_value = 0  # Initialize a variable to hold the sum of all red values

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        
        # Add generated_number to each color component
        red_new = min(r + generated_number, 255)  
        green_new = min(g + generated_number, 255)
        blue_new = min(b + generated_number, 255)
        
        total_red_value += red_new 
        
        # Set the new pixel values in the new image
        new_image.putpixel((x, y), (red_new, green_new, blue_new))

# Step-3: Save the new image in the same directory
new_image.save('./chapter1out.png')

# Step-4: Here print the total red pixel value
print("Total Red Value in the new image:", total_red_value)
