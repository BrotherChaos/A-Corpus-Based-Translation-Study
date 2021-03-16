import os
file_list = os.listdir("语料库\习近平双语讲话_20210307_独立文档_元信息标注")
speeches_list = []
sign_article_list = []
interviews_list = []
for i in file_list:
    if i.startswith("speeches"):
        speeches_list.append(i)
    elif i.startswith("articles"):
        sign_article_list.append(i)
    else:
        interviews_list.append(i)

print(len(speeches_list))
print(len(sign_article_list))
print(len(interviews_list))

with open("试验数据\表1_统计文档\speeches.txt", "w", encoding="utf-8") as f1:
    for i in speeches_list:
        path = os.path.join("语料库\习近平双语讲话_20210307_独立文档_元信息标注",i)
        with open (path, "r", encoding= "utf-8") as f2:
            f1.write(f2.read())

with open("试验数据\表1_统计文档\sign_article.txt", "w", encoding="utf-8") as f1:
    for i in sign_article_list:
        path = os.path.join("语料库\习近平双语讲话_20210307_独立文档_元信息标注",i)
        with open (path, "r", encoding= "utf-8") as f2:
            f1.write(f2.read())

with open("试验数据\表1_统计文档\interviews.txt", "w", encoding="utf-8") as f1:
    for i in interviews_list:
        path = os.path.join("语料库\习近平双语讲话_20210307_独立文档_元信息标注",i)
        with open (path, "r", encoding= "utf-8") as f2:
            f1.write(f2.read())



   


