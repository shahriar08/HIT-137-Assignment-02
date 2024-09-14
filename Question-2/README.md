"HIT-137-Assignment-02"

**Question 2: The Chamber of Strings**

### Step-by-Step Guide to Solve the Problem:

#### Step 2: Write the Python Code

Here’s a step-by-step breakdown of the code.

1. **Separate the String:**
   - Loop through the string and classify each character as a number or letter.

2. **Convert Even Numbers to ASCII:**
   - For each even number in the number substring, convert it to an ASCII decimal value.

3. **Convert Uppercase Letters to ASCII:**
   - For each uppercase letter in the letter substring, convert it to its ASCII decimal value.

Here’s the full Python code:

```python
def process_string(s):
    # Step 1: Separate the string into numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Step 2: Convert even numbers to ASCII code decimal values
    even_numbers_ascii = [ord(str(int(char))) for char in number_string if int(char) % 2 == 0]
    
    # Step 3: Convert uppercase letters to ASCII code decimal values
    uppercase_ascii = [ord(char) for char in letter_string if char.isupper()]

    return number_string, letter_string, even_numbers_ascii, uppercase_ascii

# Example input
s = '56aAww1984sktr235270aVnm145ss785fsq31DD'

# Process the string
number_string, letter_string, even_numbers_ascii, uppercase_ascii = process_string(s)

# Output the results
print(f"Number substring: {number_string}")
print(f"Letter substring: {letter_string}")
print(f"Even numbers ASCII values: {even_numbers_ascii}")
print(f"Uppercase letters ASCII values: {uppercase_ascii}")
```

### Explanation of the Code:
- **Step 1**: We used list comprehensions to separate the string into `number_string` and `letter_string`.
  - `number_string` contains only digits using `char.isdigit()`.
  - `letter_string` contains only letters using `char.isalpha()`.

- **Step 2**: We filtered even numbers from `number_string` and used `ord()` to convert each even number into its ASCII decimal value.

- **Step 3**: For `letter_string`, we filtered out uppercase letters using `char.isupper()` and converted them to ASCII decimal values using `ord()`.

---

