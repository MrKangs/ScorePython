#Before you start the program, you need to go to cmd
#and write 'pip install Xlsxwriter' and  'pip install Xlrd'

#엑셀과 파이썬 사용 전에 무조권 cmd에 들어가서 'pip install Xlsxwriter' 그리고 'pip install xlrd' 라고 쳐야함!
#Reference: https://xlsxwriter.readthedocs.io/ 
# https://www.blog.pythonlibrary.org/2014/04/30/reading-excel-spreadsheets-with-python-and-xlrd/
#and https://automatetheboringstuff.com/appendixa/ 


##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter, xlrd


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()