def process_string(s):
    # Step-1: Separate the input string into numbers and letters
    numbers_string = ''.join([char for char in s if char.isdigit()])
    letters_string = ''.join([char for char in s if char.isalpha()])

    # Step-2: Convert the even numbers to ASCII code decimal values
    even_numbers_ascii = [ord(str(int(char))) for char in numbers_string if int(char) % 2 == 0] 
    # Step-3: Convert uppercase letters to ASCII code decimal values
    uppercase_ascii = [ord(char) for char in letters_string if char.isupper()]

    return numbers_string, letters_string, even_numbers_ascii, uppercase_ascii

# Example input from the question
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
# Process the input string
numbers_string, letters_string, even_numbers_ascii, uppercase_ascii = process_string(s)
# Output
print(f"Number substring: {numbers_string}")
print(f"Letter substring: {letters_string}")
print(f"Even numbers ASCII values: {even_numbers_ascii}")
print(f"Uppercase letters ASCII values: {uppercase_ascii}")
