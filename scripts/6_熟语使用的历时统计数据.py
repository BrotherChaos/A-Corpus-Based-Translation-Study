import openpyxl
wb = openpyxl.load_workbook("试验数据\meta_data_0307.xlsx")
sheet_name_list = wb.get_sheet_names()
for sheet_name in sheet_name_list:
    print(sheet_name)
    sheet = wb.get_sheet_by_name(sheet_name)
    max_row = sheet.max_row
    time = []
    time_dict = {}
    for i in range(max_row):
        time.append(sheet["C{}".format(i+1)].value)
    # print(len(time)) 
    for i in range(8):
        time_dict["{}".format(2013+i)] = time.count("{}".format(2013+i))
    print(time_dict)
    


