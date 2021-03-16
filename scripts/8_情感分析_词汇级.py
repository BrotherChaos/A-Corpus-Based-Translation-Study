import jiagu,openpyxl
from snownlp import SnowNLP

# jiagu 提供的情感分析功能
"""
wb = openpyxl.load_workbook("试验数据\附录_词频统计.xlsx")
sheet_list = wb.get_sheet_names()
for sheet_name in sheet_list:
    sheet = wb.get_sheet_by_name(sheet_name)
    a = sheet.max_row
    for i in range(a):
        item = sheet["A{}".format(i+1)].value
        
        
        sheet["B{}".format(i+1)],sheet["C{}".format(i+1)] = jiagu.sentiment(item)
wb.save("试验数据\附录_情感分析.xlsx")
"""

# snownlp提供的情感分析功能

wb = openpyxl.load_workbook("试验数据\附录_情感分析.xlsx")

sheet_list = wb.get_sheet_names()
for sheet_name in sheet_list:
    sheet = wb.get_sheet_by_name(sheet_name)
    a = sheet.max_row
    for i in range(a):
        item = sheet["A{}".format(i+1)].value
        s = SnowNLP(item).sentiments
        sheet["D{}".format(i+1)] = s

wb.save("试验数据\附录_情感分析_snowNLP.xlsx")








