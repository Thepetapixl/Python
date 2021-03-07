import re

patterns = input()

text = "The nation is facing difficult condition. We, the youth of nation should be resposible enough to take resposibility."

print('Searching for "%s" in paragraph!' % (patterns),)

if re.search(patterns, text):
    print('Matched!')
else:
    print('Not Matched!')
    







