import os
import sys
path = input("Введите путь к папке: ")
word = input("Введите ключевое слово: ")
if not os.path.isdir(path):
    print("Нет такой папки!")
    sys.exit()
os.chdir(path)
files=[]
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать файлы
    for filename in filenames:
        if word in filename:
            files+=[filename]
            print(dirpath+"/"+filename)
print("Что Вы хотите сделать?\n1. Замена искомого слова\n2. Удаление искомого слова из файлов")
choose = input()
if choose == "1":
    w = input("Замена: ")
    for i in files:
        os.rename(i, i.replace(word, w))
if choose == "2":
    for i in files:
        os.rename(i, i.replace(word, ""))