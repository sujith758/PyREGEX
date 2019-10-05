import re

text = "Hey buddy, Hey brother"
pattern = re.findall(r'brother',text)
print(pattern)


#positive Lookahead
text = "Hey buddy, Hey brother"
pattern = re.compile("Hey(?=\sbrother)")
match = pattern.search(text)
print(match.span())

#Negative lookahead
text = "Hey buddy, Hey brother"
pattern = re.compile("Hey(?!\sbrother)")
match = pattern.search(text)
print(match.span())
