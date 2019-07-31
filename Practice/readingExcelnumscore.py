import openpyxl
import statistics as stats

num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

# Another way to print data

total = []
for x in range(2, 34):  #replace 34 for counter
    rawdata = sheet['A' + str(x)].value
    print(rawdata)
    total.append(rawdata)

print("The mean is ", stats.mean(total))


# It will print as a the same format in Excel 
# {1:10} --> 1 = which row data, 10 = how many space from space 0 or between data
# (Caution!: if one of the cell is empty as the program reads it, 
# it will return an error when it prints in the output)

