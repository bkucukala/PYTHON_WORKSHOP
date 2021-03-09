# -*- coding: utf-8 -*-

a = 1

while (a < 40):
    if (a == 21):
        break
    print(a)
    a = a + 1

#%%

for i in range(1,40):
    if (i == 10):
        break
    print(i)

#%%


while True:
    print("Girecek kimse kalmaz ise 'Ç' ye basınız..")
    a = input("Lütfen isminizi giriniz: ")
    if (a == "Ç"):
        break
    print("Hoşgeldin",a)





