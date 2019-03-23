#! python 3

# Opens a spreadsheet and writes the cells of column A into one text file,
# TODO other cells into another text file
import openpyxl

wb = openpyxl.load_workbook("produce_v2.xlsx")
wb_sheet = wb.get_active_sheet()

text_file = open("Convert_to_text.txt", "w+")

rows = wb_sheet.max_row

for cell in wb_sheet["A"]:
    text_file.write(cell.value+"\n")

text_file.close()
