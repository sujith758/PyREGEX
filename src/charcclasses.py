import re

# TO find the numbers in a string using findall()
Text = "2008,2009,2018,2010,2011,2013,2015,2017"
pattern = re.findall(r"\d{1,4}",Text)
print(pattern)


# TO match the data present in string using match()
text = "Hello world"
pattern = re.match(r"Hello",text)
print(pattern)

# TO see the span() of matched data by indexing
text = "Hello world"
pattern = re.match(r"Hello",text)
pattern1 = pattern.span()
print(pattern1)

# TO see where the search started by indexing with match()
text = "Hello world"
pattern = re.match(r"Hello",text)
pattern1 = pattern.start()
print(pattern1)

# TO see where the search ended by indexing with match()
text = "Hello world"
pattern = re.match(r"Hello",text)
pattern1 = pattern.end()
print(pattern1)

# To search data in string using search
text = "Hello world"
pattern = re.search(r"Hello",text)
print(pattern)

# To select all using findall() which prints as list
text = "Hello world"
pattern = re.findall(r"world", text)
print(pattern)

# TO Return text as an iterator of the Match objects.
text = "say hello world"
matches = re.finditer(r"say hello world",text)
for items in matches:
    print(items.span())

#TO print metacharacters use backslash before them:\$
text = "This book costs $15."
pattern = re.findall(r"\$15",text)
print(pattern)
