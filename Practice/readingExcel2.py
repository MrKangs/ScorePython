import openpyxl
import statistics as stats
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

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


print((totalx))
print((totaly))

#plt.plot(totaly,totalx)

plt.bar(totaly,totalx)

plt.show()
num.save("num.xlsx")
