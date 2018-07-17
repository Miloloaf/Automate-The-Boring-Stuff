#! python3
import re

# strip() using regex

text = str(input("Enter text to strip: "))
stripper = str(input("Enter strip string: "))
if len(stripper) == 0:
    stripper = " "

startRegex = re.compile(r'^(%s*)(.*)'%(stripper))
endRegex = re.compile(r'(%s)*$'%(stripper))

def regstrip(text):
    mo = startRegex.search(text)
    frontstrip = mo.group(2)
    mo1 = endRegex.sub("", frontstrip)
    return(mo1)

print()
print(regstrip(text))
