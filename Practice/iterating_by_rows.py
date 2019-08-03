from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67),
    (35, 73, 26),
    (92, 29, 47)
)

for row in rows:
    sheet.append(row)
# entering the data in the excel file

for row in sheet.iter_rows(min_row = 1, min_col = 1, max_row = 9, max_col = 4):
# when you setup more than the bounderies, then it will return none    
    for cell in row:
        print(cell.value, end= " ")
    print()
# reading and printing the data in the output

book.save('iterbyrows.xlsx')