#Before you start the program, you need to go to cmd
#and write 'pip install openpyxl'

#엑셀과 파이썬 사용 전에 무조권 cmd에 들어가서 'pip install openpyxl' 라고 쳐야함!
#Reference: http://zetcode.com/articles/openpyxl/ 

# Row = vertical, column = horizontal


from openpyxl import Workbook  
# A workbook is the container for all other parts of the document.

import time
#Adding time

book = Workbook()
# We create a new workbook. 
# A workbook is always created with at least one worksheet.

sheet = book.active
# We get the reference to the active sheet.

sheet['A1'] = 56
sheet['A2'] = 43
sheet['B1'] = 59
sheet['B2'] = 74
# We write numerical data to cells A1, A2, B1, and B2

now = time.strftime("%x")
sheet['A3'] = now
#Add current date in A3

sheet.cell(row = 3, column = 2).value = 2
# This statement is same as (sheet['B3'] = 2)

rows = (
    (88,46,57),
    (89,38,12),
    (23,59,78),
    (56,21,98),
    (24,18,43),
    (34,15,67)

)

for row in rows:
    sheet.append(row)
# The whole process will start submitting 
# the data from the empty row 
# (in this case, it will add data in row 4,5,6,7,8,9)

# TODO: Need to know how to replace data that has data already in that cell

book.save("sample.xlsx")
#We write the contents to the sample.xlsx file with the save() method

#--------------------------------------------------------------------------------#


