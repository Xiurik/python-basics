import re

text = "Hello my friend, lets have some fun! Mr. RORI901006Q40"
pattern = re.compile(r"\bf[a-z]*\b")
pattern2 = re.compile(r"([a-zA-Z]{3,4})(\d{6})([a-zA-Z\d]{3})")
exist = re.search("f", text)

# tell us where the string occurs as a tuple (first one found)
# print(exist.span())

# when the text starts
# print(exist.start())

# show us where it ends
# print(exist.end())

# return the string where it was the match
# print(exist.group())

# search for the match
print(pattern2.search(text))

# return all the words that matches
print(pattern2.findall(text))

# return the match only if it matches the whole string
print(pattern2.fullmatch(text))

# return the match only if it matches the beginning of the string
print(pattern2.match(text))
