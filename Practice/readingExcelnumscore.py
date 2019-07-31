import openpyxl

num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

# Another way to print data

for x in range(2, 34):  #replace 34 for counter
    print(sheet['A' + str(x)].value)


# It will print as a the same format in Excel 
# {1:10} --> 1 = which row data, 10 = how many space from space 0 or between data
# (Caution!: if one of the cell is empty as the program reads it, 
# it will return an error when it prints in the output)

