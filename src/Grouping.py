import re
#Grouping
text = "abbbbbabbbb"
pattern1 = re.findall("ab+",text)
pattern2 = re.findall("(ab)+",text)
print(pattern1)
print(pattern2)

#Grouping
text = "my name is ram my name is sam"
pattern1 = re.findall("my name is ram|sam",text)
pattern2 = re.findall("my name is (ram|sam)",text)
print(pattern1)
print(pattern2)

#Grouping
text = "12/02/2019"
pattern = re.compile("(\d{2})\/(\d{2})\/(\d{4})")
ptn = pattern.match(text)
print(ptn)
print(ptn.group())
print(ptn.group(1))
print(ptn.group(2))
print(ptn.group(3))

