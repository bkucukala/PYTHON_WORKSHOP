# -*- coding: utf-8 -*-

liste = [1,2,3,4,5,6,7,8,9]

liste.append(121)

liste.append("Metin")

print(liste)

#%%


liste1 = [1,2,3,4,5,6,7,8,9]

liste1.pop()

liste1.pop(3)

print(liste1)

#%%

liste2 = [56,78,1002,780,1,5,950]

liste2.sort()

print(liste2)

liste2.sort(reverse = True)

print(liste2)

#%%


liste3 = ["Ahmet","Mehmet","Java","Php","Html"]

liste3.sort()

print(liste3)

#%%



liste4 = [["Ahmet","Mehmet"],[1,2],["JavaScript","Php"],[14.5,7.2]]

print(liste4[2][0])

print(liste4[2])

liste4[2][0] = "Python"

print(liste4)
























