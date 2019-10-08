#Importing modules datetime,regex,sys
import datetime
import re
import sys

#passing arguments<Textfile>
arg1 = sys.argv[1]

#reading file name
text = arg1

#Using regex to search in filename and capture in groups
matching = re.search(r'(\d{8,})(\d{8})(\d{5})', text)
grp2 = matching.group(2)
grp3 = matching.group(3)

#Error handling with try,except and finally
try:
    date = datetime.datetime.strptime(grp2, '%Y%m%d').date()
    time = datetime.datetime.strptime(grp3, '%H%M%S').time()
    print(date)
    print(time)

except ValueError as error:
    print("Unknown date and time format")
    sys.exit()
finally:
    if grp2 == matching.group(2):
        print(text)
    else:
        print(grp2)
        print(grp3)







# Alias_20191002162323.xlsx
# Abc333455562019093433455.txt
