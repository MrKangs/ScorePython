import openpyxl

book = openpyxl.load_workbook('sample.xlsx')

sheet = book.active

cells = sheet['A1' : 'B6']
#Reading from cells A1 to B6

for c1, c2 in cells:
    print("{0:8} {1:8}".format(c1.value, c2.value))

# It will print as a the same format in Excel 
# (Caution!: if one of the cell is empty as the program reads it, it will return an error when it prints in the output)

