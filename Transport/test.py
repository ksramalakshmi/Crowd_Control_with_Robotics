import openpyxl

doc = openpyxl.load_workbook("bus.xlsx")
sheet = doc.active

cell1 = sheet.cell(row= 5, column=2)

try:
    cell1.value += 1
except:
    cell1.value = 1

doc.save("bus.xlsx")
doc.close