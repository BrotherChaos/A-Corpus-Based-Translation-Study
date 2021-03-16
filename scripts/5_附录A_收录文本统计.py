import os, openpyxl
name_list = open("试验数据\附录A_收录文本统计.txt","r",encoding="utf-8").readlines()
wb = openpyxl.Workbook()
sheet = wb.create_sheet()
for i in range(len(name_list)):
    content_list =name_list[i].split("_")
    print(content_list)
    
    sheet["A{}".format(i+1)] = content_list[0]
    sheet["B{}".format(i+1)] = content_list[1]
    sheet["C{}".format(i+1)] = content_list[2]
wb.save("试验数据\附录A_收录文本统计.xlsx")
