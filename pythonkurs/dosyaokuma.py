# -*- coding: utf-8 -*-

file = open("deneme.txt","r",encoding="utf-8")

for i in file:
    print(i,end="")

a = file.read()

print(a)

print(file.readline())

print(file.readlines())

file.close()

