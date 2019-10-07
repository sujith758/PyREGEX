import datetime
import re
text ='Alias_20191002162323.xlsx'
matching = re.search(r'(\d{8})(\d{6})', text)
print(matching.group(1))
print(matching.group(2))
# print(matching.group(3))
dateformat = '%Y%m%d'
timeformat = '%H%M%S'

date = datetime.datetime.strptime(matching.group(1), '%Y%m%d').date()
time = datetime.datetime.strptime(matching.group(2), '%H%M%S').time()



if datetime.date != dateformat:
    print("Invalid date format")
else:
    print(date)
if datetime.time != timeformat:
    print("Invalid time format")
else:
    print(time)


# Alias_20191002162323.xlsx
# Abc333455562019093433455.txt
