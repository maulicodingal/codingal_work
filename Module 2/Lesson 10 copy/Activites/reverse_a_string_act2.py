print("Welcome to a program that reverses a string!\n\n")

word = input("Give me a string: ")

print("Your word is :", text)


reversing_word = ""

"""
1st-G - G


"""

size = len(word)
size-=1

while (size>=0):
    reversing_word = reversing_word + text[size]
    size-=1

# for nyon in word:
# reversing_word = nyon + reversing_word

print("The reversed string is:", reversing_word)