import openpyxl
import statistics as stats
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.patches import Polygon
import pandas as pd
import seaborn as sea
from pandas import read_csv

#Setup----------------------------------------------------------------------------------------
font_name = fm.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
totalx = [] #학생 이름들
totaly = [] #학생 성적들

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

counter = int(input("How many students' data do you have?: "))
location_for_score = str(input("Which column the scores are located?: "))
location_for_name = str(input("Which column the names are located?: "))
print("Go to the file propreties and copy the file location.")
print("Then enter the path below with the file name.")
location_for_file = str(input("Where is the excel file location(enter the path)?: "))


excel_file = openpyxl.load_workbook(str(location_for_file))

sheet = excel_file.active

#Calculations----------------------------------------------------------------------------------    


for x in range(0, counter): 
    rawdatax = sheet[str(location_for_name) + str(x + 2)].value
    print(rawdatax)
    totalx.append(rawdatax)

for y in range(0, counter): 
    rawdatay = sheet[str(location_for_score) + str(y + 2)].value
    print(rawdatay)
    totaly.append(rawdatay)


Mean = stats.mean(totaly)
Median = stats.median(totaly) #Center
Sd = stats.stdev(totaly) 
Min = min(totaly)
Max = max(totaly)
Variance = stats.variance(totaly)
q1 = np.quantile(totaly, .25)
q3 = np.quantile(totaly, .75)

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


#Chart-----------------------------------------------------------------------------------------
plt.figure(1)
plt.plot(totalx,totaly)
plt.bar(totalx,totaly)  #(학생 이름(x-value),학생 성적(y-value))
plt.figure(2)
plt.boxplot(totaly)

plt.show()
excel_file.save(str(location_for_file))

#TODO: 다양한 종류의 챠트 와 한창에서 표현, 그래프 색변경, 3년의 같은 데이트를 한 창에서 표현, 타이틀 및 단위