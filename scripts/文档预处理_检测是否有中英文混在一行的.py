import os
file_name_list = os.listdir("语料库\习近平双语讲话_20210228_独立文档_元信息标注")
file_path_list = []
for file_name in file_name_list:
    file_path_list.append(os.path.join("语料库\习近平双语讲话_20210228_独立文档_元信息标注",file_name))
for f in file_path_list:
    with open(f,"a", encoding="utf-8") as f1:
        f1.write("\n")
