# def is_palindrome(text):
#     # Remove spaces and convert to lowercase
#     cleaned_text = text.replace(" ", "").lower()
#
#     # Check if the cleaned text is the same forwards and backwards
#     return cleaned_text == cleaned_text[::-1]
#
# # Get input from the user
# text = input("Enter some text: ")
#
# # Check if the text is a palindrome
# if text and is_palindrome(text):
#     print("The text is a palindrome.")
# else:
#     print("The text is not a palindrome.")

# using for loop
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()

    # Check for palindrome using a loop
    # length = len(cleaned_text)
    # for i in range(length // 2):
    #     if cleaned_text[i] != cleaned_text[length - i - 1]:
    #         return False
    # return True

    # check for palindrom using while loop
    while len(cleaned_text) > 1:
        if cleaned_text.popleft() != cleaned_text.pop():
            return False
    return True


# Get input from the user
text = input("Enter some text: ")

# Check if the text is a palindrome
if text and is_palindrome(text):
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")
