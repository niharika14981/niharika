char = input("Enter a character: ")
if char.isupper():
    print("The character is an Uppercase letter.")
elif char.islower():
    print("The character is a Lowercase letter.")
elif char.isdigit():
    print("The character is a Digit.")
else:
    print("The character is a Special symbol.")
