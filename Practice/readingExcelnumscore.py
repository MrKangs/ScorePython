import openpyxl
import statistics as stats

num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

counter = int(input("How many students' data do you have?"))
total = []

for x in range(0, counter):  #replace 33 for counter
    rawdata = sheet['A' + str(x + 2)].value
    print(rawdata)
    total.append(rawdata)

num_mn = stats.mean(total)

sheet['A' + str(counter + 2)] = "Mean:"
sheet['B' + str(counter + 2)] = num_mn
num.save("num.xlsx")
