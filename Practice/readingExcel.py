import openpyxl

book = openpyxl.load_workbook('sample.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']
print(a1.value, a2.value)
# printing the A1 and A2 data 

a3 = sheet.cell(row = 3, column = 1)
print(a3.value)
# Another way to print data

cells = sheet['A4' : 'C9']
#Reading from cells A4 to C9

for c1, c2, c3 in cells:
    print("{0:10} {1:7} {2:5}".format(c1.value, c2.value, c3.value))

# It will print as a the same format in Excel 
# {1:10} --> 1 = which row data, 10 = how many space from space 0 or between data
# (Caution!: if one of the cell is empty as the program reads it, 
# it will return an error when it prints in the output)

