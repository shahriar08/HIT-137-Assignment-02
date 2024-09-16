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

# Example usage
key = 13  # Using ROT13 cipher as the key
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
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)