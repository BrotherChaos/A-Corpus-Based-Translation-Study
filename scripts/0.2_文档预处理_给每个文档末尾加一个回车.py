import os
file_name_list = os.listdir("语料库\习近平双语讲话_20210228_独立文档_元信息标注")
file_path_list = []
for file_name in file_name_list:
    file_path_list.append(os.path.join("语料库\习近平双语讲话_20210228_独立文档_元信息标注",file_name))

check_file = []
for f in file_path_list:
    check_lines = open(f,"r", encoding="utf-8").readlines()
    for line in check_lines:
        eng = [",","?",".","!"]
        chi = ["，","。", "？","！"]
        for e in eng:
            for c in chi:
                if e in line and c in line:
                    check_file.append([f,line])

with open ("待修改文献.txt", "w", encoding="utf-8") as f2:
    for thing in check_file:
        f2.write(thing[0] + "\n" + thing[1])

