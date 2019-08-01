import openpyxl
import statistics as stats
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)


num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

counter = int(input("How many students' data do you have?: "))
location = str(input("Which column the scores are located?: "))

total = []

for x in range(0, counter): 
    rawdata = sheet[str(location) + str(x + 2)].value
    print(rawdata)
    total.append(rawdata)

Mean = stats.mean(total)
Median = stats.median(total)
SD = stats.stdev(total)
Min = min(total)
Max = max(total)
Variance = stats.variance(total)

sheet['A' + str(counter + 2)] = "Mean:"
sheet['B' + str(counter + 2)] = Mean

sheet['A' + str(counter + 3)] = "Median:"
sheet['B' + str(counter + 3)] = Median

sheet['A' + str(counter + 4)] = "Max:"
sheet['B' + str(counter + 4)] = Max

sheet['A' + str(counter + 5)] = "Min:"
sheet['B' + str(counter + 5)] = Min

sheet['A' + str(counter + 6)] = "Standard Deviation:"
sheet['B' + str(counter + 6)] = SD

sheet['A' + str(counter + 7)] = "Variance:"
sheet['B' + str(counter + 7)] = Variance

num.save("num.xlsx")
