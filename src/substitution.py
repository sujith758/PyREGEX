
import re
#Substituting selected words from a string
text = "cat mat hat bat dat sat"
pattern = re.compile(r"\w+")
ptn = pattern.sub("food",text)
print(ptn)
