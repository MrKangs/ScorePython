import openpyxl
import statistics as stats

num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

counter = int(input("How many students' data do you have?: "))
location = str(input("Which column the scores are located?: "))

total = []

for x in range(0, counter): 
    rawdata = sheet[str(location) + str(x + 2)].value
    print(rawdata)
    total.append(rawdata)

num_mn = stats.mean(total)

sheet['A' + str(counter + 2)] = "Mean:"
sheet['B' + str(counter + 2)] = num_mn
#TODO: Max, Min, median, SD is necessary
num.save("num.xlsx")
