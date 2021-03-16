import os, openpyxl


# 将能找到的熟语数量及其出现次数写在一个词典里，例如{"一往无前"：30，"改革开放":40}
# 将要检索的正文的路径以列表的方式返回
# 最终返回一个元组({},[])
def sum_result(idiom_file, file_dir):
    # 将能找到的熟语数量写在一个列表里
    result_dic = {}
    file_path_list = []
    file_list = []
    idiom_list = open(idiom_file,"r", encoding="utf-8").read().split("\n")
    search_file_name_list = os.listdir(file_dir)

    for file_name in search_file_name_list:
        file_path_list.append(os.path.join(file_dir,file_name))
    print(file_path_list)
    
    for file_path in file_path_list:
        file_list.append(open(file_path,"r",encoding="utf-8").read())
    merged_file = "".join(file_list)

    for idiom in idiom_list:
        counts = merged_file.count(idiom)
        if counts > 0:
            # print("{}  出现的次数为  {}".format(idiom,counts))
            result_dic[idiom] = counts   

    return result_dic , file_path_list


# 返回一个列表,[[元信息]]
def meta_data(appeared_idiom_dic, file_path_list):
    meta_data_list = []
    for idiom in list(appeared_idiom_dic.keys()):      
        for file_path in file_path_list:        
            txt = open("{}".format(file_path),"r",encoding="utf-8").readlines()
            for line in txt:
                # 看看每一行包含要检索的词条几次，包含几次就打印几次
                if line.count(idiom) > 0: 

                    types = file_path.split("_")[-3][6:]
                    time  = file_path.split("_")[-2]
                    name  = "_".join(file_path.split("_")[-3:])[6:]
                    next_line = txt[txt.index(line) + 1]
                    
                    print(idiom)
                    # print(types)
                    # print(time)
                    # print(txt_name)
                    print(line[:-1])
                    print(next_line)
                    value_list = ["条目："+ idiom, "类型："+types, "时间："+ time, "文件名："+ name, "中文："+ line[:-1], "英文："+ next_line]
                    for count in range(line.count(idiom)):
                        meta_data_list.append(value_list)
    print(meta_data_list)
    print("列表生成完成，共计 {} 条结果。".format(len(meta_data_list)))
    return meta_data_list


# 将元信息写入 xlsx 表格
def to_excel(meta_data_list,sheet_name, xlsx_file_path):
    # 载入表格
    wb = openpyxl.load_workbook(xlsx_file_path)
    # 新建页
    sheet = wb.create_sheet(sheet_name)
    # 填写表头
    sheet["A1"] = "条目"
    sheet["B1"] = "类型"
    sheet["C1"] = "时间"
    sheet["D1"] = "文件名"
    sheet["E1"] = "中文"
    sheet["F1"] = "英文"

    for i in range(len(meta_data_list)):
        spec_item_list = meta_data_list[i]
        sheet["A{}".format(i+2)] = spec_item_list[0][3:]
        sheet["B{}".format(i+2)] = spec_item_list[1][3:]
        sheet["C{}".format(i+2)] = spec_item_list[2][3:]
        sheet["D{}".format(i+2)] = spec_item_list[3][4:]
        sheet["E{}".format(i+2)] = spec_item_list[4][3:]
        sheet["F{}".format(i+2)] = spec_item_list[5][3:]
    wb.save(xlsx_file_path)



"熟语词表\成语词表_20200617.txt"
idiom_file_list = ["熟语词表\成语词表_20200617.txt","熟语词表\格言词表_20200617.txt","熟语词表\惯用语词表_20200617.txt","熟语词表\谚语词表_20200617.txt"]
sheet_name_list = ["成语元信息","格言元信息","惯用语元信息","谚语元信息"]

for i in range(4):
    a = sum_result(idiom_file_list[i],"语料库\习近平双语讲话_20210307_独立文档_元信息标注")
    b = meta_data(*a)
    to_excel(b,sheet_name_list[i],"meta_data_0307.xlsx")







