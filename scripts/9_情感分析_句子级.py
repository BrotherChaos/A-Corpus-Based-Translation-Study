import jiagu,openpyxl,re
from snownlp import SnowNLP

# jiagu 提供的情感分析功能
"""
wb = openpyxl.load_workbook("试验数据\meta_data_0309.xlsx")
sheet_list = wb.get_sheet_names()
for sheet_name in sheet_list:
    sheet = wb.get_sheet_by_name(sheet_name)
    max_raw = sheet.max_row
    for i in range(max_raw-1):
        item = sheet["A{}".format(i+2)].value
        sentence_para = sheet["E{}".format(i+2)].value
        
        sentence_list = re.split(r'[；。！？]',sentence_para)
        for sentence in sentence_list:
            if item in sentence:
                sheet["F{}".format(i+2)] = sentence
                sheet["G{}".format(i+2)],sheet["H{}".format(i+2)] = jiagu.sentiment(sentence)


wb.save("试验数据\9_meta_data_0309_情感分析.xlsx")
"""

# snownlp提供的情感分析功能

wb = openpyxl.load_workbook("试验数据\9_meta_data_0309_情感分析.xlsx")

sheet_list = wb.get_sheet_names()
for sheet_name in sheet_list:
    sheet = wb.get_sheet_by_name(sheet_name)
    max_row = sheet.max_row
    for i in range(max_row-1):

        item = sheet["F{}".format(i+2)].value
        s = SnowNLP(item).sentiments
        sheet["J{}".format(i+2)] = s

wb.save("试验数据\9_附录_情感分析_snowNLP.xlsx")








