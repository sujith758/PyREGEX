import re
#Using escape() to print backslashes from text
text = "C:\Windows\System32"
print("C:\\Windows\\System32")
pattern = re.search(re.escape("C:\Windows\System32"),text)
print(pattern)
