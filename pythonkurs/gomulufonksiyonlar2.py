# -*- coding: utf-8 -*-

a = ["Civan","Hasan","Betül","Ali"]

print(list(reversed(a)))

#%%


print(sorted("Python"))

print(sorted(("pazartesi","salı","çarşamba")))

#%%


a = [1,2,3]
b = ["a","b","c"]

print(*zip(a,b))

print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i,j)

#%%

from functools import reduce

liste = [1,2,3,4,5]

a = reduce(lambda x,y : x*y,liste)
print(a)

#%%

from functools import reduce

liste1 = [1,2,3,4,5,6]

b = reduce(lambda x,y: x+y,liste1)
print(b)





















