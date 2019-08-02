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
location_for_score = str(input("Which column the scores are located?: "))
location_for_name = str(input("Which column the names are located?: "))
total = []

def switch_for_chart(number):
    if(number == 'A'):
        return 1
    elif(number == 'B'):
        return 2
    elif(number == 'C'):
        return 3
    elif(number == 'D'):
        return 4
    elif(number == 'E'):
        return 5
    elif(number == 'F'):
        return 6
    elif(number == 'G'):
        return 7
    elif(number == 'H'):
        return 8    
    


for x in range(0, counter): 
    rawdata = sheet[str(location_for_score) + str(x + 2)].value
    print(rawdata)
    total.append(rawdata)

Mean = stats.mean(total)
Median = stats.median(total)
Sd = stats.stdev(total)
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
sheet['B' + str(counter + 6)] = Sd

sheet['A' + str(counter + 7)] = "Variance:"
sheet['B' + str(counter + 7)] = Variance


#TODO: Chart location user input, chart name label represent, and reading files in different location

chart = ScatterChart()

xvalues = Reference(sheet, min_col = switch_for_chart(location_for_name), min_row = 2, max_row = (counter + 1))

yvalues = Reference(sheet, min_col = switch_for_chart(location_for_score), min_row = 2, max_row = (counter + 1))

series = Series(values = yvalues, xvalues = xvalues, title = "2019 중간고사 성적")

chart.series.append(series)

chart.title = "Number Theory 2019 Middle Term"

chart.x_axis.title = "학생 이름"

chart.y_axis.title = "학생 성적"

sheet.add_chart(chart, "E36")

num.save("num.xlsx")
