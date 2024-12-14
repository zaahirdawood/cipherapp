from re import split
import string

# Get lowercase alphabet
lowercase = string.ascii_lowercase

# def cipher_pattern(text, lowercase pattern=*args):

#     text = text.lower()
#     text = text.replace(" ", "")

#     return text

text = input("Enter a string: ")


final = ""
for i in list(text):
    for x, alpha in enumerate(lowercase):  # lowercase:
        if i == alpha:
            final += "".join(lowercase[x + 1])

print(final, text)
