#! python3

""" Takes a list of list of strings and displays it in a well-organized
table with each column right justified"""

def longest(list):
    length = 0

    for item in list:
        if len(item) > length:
            length = len(item)

    return length

def table(mylist):
    longestitems = []
    tempstring = ""
    listlen = 0

    for innerlist in mylist:
        longestitems.append(longest(innerlist))
        listlen = len(innerlist)

    for i in range(listlen):
        for x in range(len(mylist)):
            tempstring += mylist[x][i].rjust(longestitems[x] + 1, " ")
        print(tempstring)
        tempstring = ""

    return ""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

print(table(tableData))
