# -*- coding: utf-8 -*-

with open("deneme.txt","r+",encoding="utf-8") as file:
    file.seek(4)
    file.write("file")

#with open("deneme.txt","a",encoding="utf-8") as file:
    
    #file.write("Hava Çok Güzel")
    
with open("deneme.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(2, "Bugün Yola Çıkıyorum\n")
    file.seek(0)
    for i in liste:
        file.write(i)
    
with open("deneme.txt","r+",encoding="utf-8") as file:    
    print(file.read())
    
    