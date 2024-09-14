"HIT-137-Assignment-02"

### Step-by-Step Guide to Solve the Problem:

**Chapter 1: The Gatekeeper(chamber_of_strings.py)**

To solve the gatekeeper problem, we must separate the string. Loop through the string and classify each character as a number or letter. We must convert even numbers to ASCII. Where for each even number in the number substring, convert it to an ASCII decimal value. Also convert uppercase letters to ASCII. For each uppercase letter in the letter substring, convert it to its ASCII decimal value. 

Step 1: We used list comprehensions to separate the string into number_string and letter_string. 

   number_string contains only digits using char.isdigit(). 

   letter_string contains only letters using char.isalpha(). 

Step 2: We filtered even numbers from number_string and used ord() to convert each even number into its ASCII decimal value. 

Step 3: For letter_string, we filtered out uppercase letters using char.isupper() and converted them to ASCII decimal values using ord(). 

Step 4: After running the code, we can see the output on the terminal. 

 

**Chapter 2: The Chamber of Strings(image_processor.py)**

To solve the Chamber of Strings problem,, we have to follow below steps:  

Step 1: We must generate a random number. The code generates a number using the current time, adds 50, and adjusts it to be an even number. This generated number will be used for modifying pixel values. 

Step 2: Load the Image from the directory. The Image.open() function from the Pillow library is used to load the provided image (chapter1.jpg). We load the pixel data using the load() function to access individual pixel values. 

Step 3: Then Modify Pixel Values. For each pixel in the image, we add the generated number to the red, green, and blue components of the pixel, ensuring that no value exceeds 255. 

Step 4: After that, save the modified image. The modified pixels are saved into a new image file called chapter1out.png. 

Step 5: Sum of Red Values. As per the instructions, the sum of all the red pixel values in the new image is calculated and printed. 

 

 