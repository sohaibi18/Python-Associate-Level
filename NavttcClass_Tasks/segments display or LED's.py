# Patterns for digits 0-9
patterns = [
    [" # ", " # ", "###", " # ", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]


def display_number(number):
    # Convert the number to a string to iterate through each digit
    digits = str(number)

    # Initialize a list to hold each row of the display
    rows = ["", "", "", "", ""]

    # Iterate through each digit
    for digit in digits:
        # Convert the digit to an integer to index into the patterns list
        d = int(digit)
        for i in range(5):
            # Append the pattern for the current digit to the corresponding row
            rows[i] += patterns[d][i] + " "

    # Print the resulting LED display
    for row in rows:
        print(row)


# Example usage:
number = int(input("Enter a non-negative integer: "))
display_number(number)
