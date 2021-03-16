import openpyxl
wb = openpyxl.load_workbook("试验数据\meta_data_0307.xlsx")
sheet_name_list = wb.get_sheet_names()
for sheet_name in sheet_name_list:
    print(sheet_name)
    sheet = wb.get_sheet_by_name(sheet_name)
    max_row = sheet.max_row
    print(max_row)
    types = []
    type_dict = {}
    for i in range(max_row):
        types.append(sheet["B{}".format(i+1)].value)
    print(len(types)) 
    type_dict["articles"] = types.count("articles")
    type_dict["speeches"] = types.count("speeches")
    type_dict["interviews"] = types.count("interviews")
    print(type_dict)
   
    


