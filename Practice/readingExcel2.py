import openpyxl
import statistics as stats
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)
from matplotlib import pyplot as plt




num = openpyxl.load_workbook('num.xlsx')

sheet = num.active

counter = int(input("How many students' data do you have?: "))
location_for_score = str(input("Which column the scores are located?: "))
location_for_name = str(input("Which column the names are located?: "))
totalx = []
totaly = []

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
    rawdatax = sheet[str(location_for_score) + str(x + 2)].value
    print(rawdatax)
    totalx.append(rawdatax)

for y in range(0, counter): 
    rawdatay = sheet[str(location_for_name) + str(y + 2)].value
    print(rawdatay)
    totaly.append(rawdatay)


print(str(totalx))
print(str(totaly))

plt.plot(str(totaly),str(totalx))
plt.show()




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
