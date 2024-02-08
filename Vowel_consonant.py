# WAP to find if a character is a vowel or consonant
ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a vowel.")
else:
    print(ch, "is a consonant.")
