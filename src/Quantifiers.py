import re
#Quantifiers ?,*,+,between {n,m}
#Using ? quantifier 0 or 1 repetition
text = "I have 2 dogs. One dog is 1 year old and other one is 2 years old. Both dogs are very cute!"
pattern = re.findall(r"dogs?",text)
print(pattern)

#Using * quantifier 0 or more times
text = "file1.txt file_one.txt file.txt fil.txt file.xml file-1.txt"
pattern = re.findall(r"file[\w-]*\.txt",text)
print(pattern)

#Using + quantifier 1 or more times
text = "file1.txt file_12.txt file.txt fil.txt file.xml file-1.txt"
pattern = re.findall(r"file[\w_-]+\d\.txt",text)
print(pattern)


text = "<html><head><title>Title</title>"
pattern = re.findall(r"<.*>",text)
print(pattern)
pattern = re.findall("<.*?>",text)
print(pattern)
