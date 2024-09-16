# Decryption function
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around within 'a' to 'z'
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around within 'A' to 'Z'
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    return decrypted_text

# Encrypted code from the image (partial)
encrypted_code = '''
tbyony_inevnoyr = 100
zl_qvpg = ['xrl1', 'inyhr1', 'xrl2', 'inyhr2', 'xrl3', 'inyhr3']
cqs erpbtf_ahzoref() :
    ybpngr_tybor() = tbyony_inevnoyr
    ybpngr_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
juvgr ybpngr_inevnoyr * 2 = 0:
    qb erpbtf_ahzoref(ahzoref=zl_fr)
'''
# Decrypting the encrypted code using the assumed key (13 for ROT13)
key = 13
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted code:")
print(decrypted_code)

# Corrected and commented decrypted code
total_inventory = 100  # Corrected variable name
my_list = ['key1', 'value1', 'key2', 'value2', 'key3', 'value3']  # Clearer naming

# Corrected function definition with recursive call caution
def process_numbers():
    stored_total = total_inventory
    current_inventory = 5
    numbers = [1, 2, 3, 4, 5]

    # Logic corrections in the loop
    while current_inventory * 2 == 0:
        process_numbers()  # Infinite recursion risk - requires base case
# Loop and logic correction for better results
total = 0
for i in range(5):
    total_inventory -= i
    current_inventory = total_inventory - 10
    my_list[i] = current_inventory * 2  # Assign current_inventory * 2 to my_list at index i

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
    
    # Output the results
print("Total Inventory:", total_inventory)
print("My List:", my_list)
print("Final Total:", total)
print("Counter:", counter)