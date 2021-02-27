import os
if not os.path.exists("f1.txt"):
    f = open("f1.txt",encoding='UTF-8',mode= "w")
    print("f1 создан. Запишите в него что-нибудь: ")
    f.write(input())
    f.close()
text = open("f1.txt").read()
c = 0
for i in text:
    if i.isalpha():
        c += 1
print("Букв: "+str(c))
spl = input("Введите разделитель:")
print(len(text.split(spl))-1)
for i in range(9):
    text = text.replace(str(i), "%")
file2 = open("f2.txt", "w")
file2.write(text)
file2.close()
