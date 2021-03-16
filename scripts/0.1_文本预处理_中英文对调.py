def row_order_change(old_file):
    file_list = open(old_file,"r",encoding="utf-8").readlines()
    first_row = file_list[0]
    to_be_changed_list = file_list[1:]
    list_eng = to_be_changed_list[::2]
    list_chi = to_be_changed_list[1::2]
    merged_list = []
    for i in range(len(list_eng)):
        merged_list.append(list_chi[i])
        merged_list.append(list_eng[i])
    new_file = open("new.txt","w+",encoding="utf-8")
    contents = "".join(merged_list)
    new_file.write(first_row)
    new_file.write(contents)
    new_file.close()

row_order_change("corpus\习近平双语讲话_20210307_独立文档_元信息标注\speeches_2016_ 习近平G20杭州峰会开幕式致辞.txt")