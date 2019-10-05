
import re
#Using | to mention search data
#Type1
text = "the most common conjunctions are and, or and but."
pattern = re.findall(r"and|or|the",text)
print(pattern)

#Type2
text = "What is your name? Who are you?"
pattern = re.findall(r"What|Who are",text)
print(pattern)

#Type3
text = "What is your name? Who is your mother?"
pattern = re.findall(r"(What|Who) is",text)
print(pattern)



