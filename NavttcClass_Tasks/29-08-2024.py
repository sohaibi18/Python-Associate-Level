# # Ceaser Cipher
# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)
#
# print(cipher)

# Ceaser cipher by shifting 2 or more digit
# Taking inputs
text = input("Enter your message: ")  # Example: abcxyzABCxyz 123
value = int(input("Enter the shift value: "))  # Example: 2

# Initialize an empty string for the ciphered text
cipher = ''

# Validate the shift value
if 1 <= value <= 25:
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            code = ord(char) + value

            # Handle uppercase letters
            if char.isupper():
                if code > ord('Z'):
                    code = code - 26  # Wrap around to 'A'

            # Handle lowercase letters
            elif char.islower():
                if code > ord('z'):
                    code = code - 26  # Wrap around to 'a'

            cipher += chr(code)
        else:
            cipher += char  # Keep non-alphabetic characters as they are
else:
    print("Enter a shift value from 1 to 25")

# Print the resulting ciphered text
print(cipher)

#
# # Caesar cipher - decrypting a message.
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)
#
# print(text)



