# -*- coding: utf-8 -*-

print(list(enumerate("Python")))

for i in enumerate("Civan"):
    print(i)
    

a = [i for i in enumerate("Hasan")]

print(a)

#%%

b = [2,5,8,9]

def kareal(x):
    return x**2

print(list(map(kareal,b)))

#%%


print(max(4,8,77))


c = [44,88,1000,5412,9999,456,2123]

print(max(c))
#%%


c = [44,88,1000,5412,9999,456,2123]
print(min(c))


#%%

print(pow(6, 2))











