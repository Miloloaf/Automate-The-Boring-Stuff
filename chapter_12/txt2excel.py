#! python 3

# Reads in the contents of a text file and inserts those contents into a spreadsheet, 
# with one line of text per row. The lines of the first text file will be in the cells of column A, 
# TODO Lines of the second text file will be in the cells of column B.

import openpyxl

text_file = r"C:\Users\User\.PyCharmCE2018.2\config\scratches\Test_Files\Test.txt"
wb = openpyxl.Workbook()
wb_sheet = wb.get_active_sheet()

with open(text_file, "r") as file:
    converted = file.read().splitlines()

for x in range(len(converted)):
    line = converted[x]
    row = x+1
    cell = "A"+str(row)
    wb_sheet[cell] = line

wb.save("test_line_convert.xlsx")


