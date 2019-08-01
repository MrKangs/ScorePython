import openpyxl
import statistics as stats

num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

# Another way to print data
counter = int(input("How many students' data do you have?"))
total = []
for x in range(0, counter):  #replace 33 for counter
    rawdata = sheet['A' + str(x + 2)].value
    print(rawdata)
    total.append(rawdata)


num_mn = stats.mean(total)
print("The mean is ", num_mn)

sheet['A' + str(counter + 2)] = "Mean:"
sheet['B' + str(counter + 2)] = num_mn
num.save("num.xlsx")


# It will print as a the same format in Excel 
# {1:10} --> 1 = which row data, 10 = how many space from space 0 or between data
# (Caution!: if one of the cell is empty as the program reads it, 
# it will return an error when it prints in the output)

