def are_anagrams(text1, text2):
    # Remove spaces, convert to lowercase, and sort the characters
    cleaned_text1 = sorted(text1.replace(" ", "").lower())
    cleaned_text2 = sorted(text2.replace(" ", "").lower())

    # Compare the sorted versions of the texts
    return cleaned_text1 == cleaned_text2


# Get input from the user
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

# Check if the texts are anagrams
if text1 and text2 and are_anagrams(text1, text2):
    print("The texts are anagrams.")
else:
    print("The texts are not anagrams.")
