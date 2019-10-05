import re

text = "today is 05/10/2019.yesterday was 04/10/2019.tomorrow will be 06/10/2019."
pattern = re.compile("(\d{2})\/(\d{2})\/(\d{4})")
newtext = pattern.sub(r"\3-\2-\1", text)
print(newtext)