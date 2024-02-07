w = input("Enter a word: ").lower().replace("", "")
palindrome = w == w[::-1]

if palindrome:
    print("This is palindrom ")
else:
    print("This is not palindrom ")    