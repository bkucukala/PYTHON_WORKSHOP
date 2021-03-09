# -*- coding: utf-8 -*-

with open("deneme.txt","r",encoding="utf-8") as file:
    
    file.seek(4)
    print(file.read(7))

    
