import openpyxl 
import statistics as stats
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series
)

from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import numpy as np

#Setup----------------------------------------------------------------------------------------
font_name = fm.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
totalx = [] #학생 이름들
totaly = [] #학생 성적들
histogram_bin_num = 10

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
    elif(number == 'I'):
        return 9
    elif(number == 'J'):
        return 10
    elif(number == 'K'):
        return 11

#User Input------------------------------------------------------------------------------------

print("*************************************************************************")
print("*           파일 속성에 들어 가서 주소를 복사하고                       *")
print("* 다음 질문에 붙어라! 그리고 파일 이름 & extension 까지 적고 enter 치라.*")
print("*************************************************************************")
location_for_file = str(input("파일은 어디에 위치 되어있어?: "))
print()
print("****************************************************************************************************")
print("*                                   원하는 그래프를 번호로 입력하라!                               *")
print("* 1＝ bar chart with line chart, 2 = box and wisker chart, 3 = histogram with best fit line chart　*")
print("****************************************************************************************************")

chart_desire = int(input("무슨 그래프를 원해?"))
print()
counter = int(input("학생수는?: "))
print()
location_for_score = str(input("점수 열는 어디?: "))
print()
location_for_name = str(input("학생 이름 명단열 어디?: "))
print()
x_axis = str(input("x축 명은?: "))
print()
y_axis = str(input("y축 명은?: "))
print()
min_unit = int(input("그래프의 최소 값은?: "))
print()
max_unit = int(input("그래프의 최대 값은?: "))
print()
units = int(input("단위 크기는? "))
print()
Title = str(input("그래프 명은?: "))
print()
chart_location = str(input("그래프 위치는 어디에?: "))


excel_file = openpyxl.load_workbook(str(location_for_file))

sheet = excel_file.active

#Calculations----------------------------------------------------------------------------------    

for y in range(0, counter): 
    rawdatay = sheet[str(location_for_score) + str(y + 2)].value
    totaly.append(rawdatay)

Mean = stats.mean(totaly)
Median = stats.median(totaly) #Center
Sd = stats.stdev(totaly) 
Min = min(totaly)
Max = max(totaly)
Variance = stats.variance(totaly)
q1 = np.quantile(totaly, .25)
q3 = np.quantile(totaly, .75)

if (chart_desire == 1 or 2):
    for x in range(0, counter): 
        rawdatax = sheet[str(location_for_name) + str(x + 2)].value
        totalx.append(rawdatax)


#Chart-----------------------------------------------------------------------------------------
if(chart_desire == 1):
    plt.figure(1)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(Title)
    plt.plot(totalx,totaly,'gs--') #plt.plot(totalx,totaly, color = 'g') --> using seaborn
    plt.bar(totalx,totaly)  #(학생 이름(x-value),학생 성적(y-value))
    plt.yticks(np.arange(min_unit, max_unit, units)) #눈금: (min, max, 단위)
    plt.savefig(Title +  str("1.png")) #TODO:graph size need to be find for saving purpose

elif(chart_desire == 2):
    plt.figure(2)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(Title)
    plt.yticks(np.arange(min_unit ,max_unit, units)) #눈금: (min, max, 단위)
    plt.boxplot(totaly)
    plt.savefig(Title +  str("2.png"))

elif(chart_desire == 3):
    plt.figure(3)
    plt.hist(totaly, histogram_bin_num, density= 1)
    plt.xlabel(y_axis)
    plt.ylabel("빈도")
    plt.title(Title)
    plt.savefig(Title +  str("3.png"))


plt.show()

#Excel-----------------------------------------------------------------------------------------

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

if(chart_desire == 1):
    img1 = openpyxl.drawing.image.Image(Title + str("1.png"))
    img1.anchor = chart_location
    sheet.add_image(img1)
elif(chart_desire == 2):
    img2 = openpyxl.drawing.image.Image(Title + str("2.png"))
    img2.anchor = chart_location
    sheet.add_image(img2)
elif(chart_desire == 3):
    img3 = openpyxl.drawing.image.Image(Title + str("3.png"))
    img3.anchor = chart_location
    sheet.add_image(img3)


excel_file.save(str(location_for_file))

#TODO:그래프 색변경, 3년의 같은 데이트를 한 창에서 표현
# https://datascienceschool.net/view-notebook/d0b1637803754bb083b5722c9f2209d0/
# https://matplotlib.org/gallery/index.html 
