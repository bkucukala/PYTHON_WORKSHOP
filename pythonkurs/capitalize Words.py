
def convert(lst): 
    Words=""
    for item in lst:
        Words+= item.capitalize() 
        Words+= " "
    return Words
      

Full_Name =  "hello   world  lol"
Full_Name=convert(Full_Name.split())
print(Full_Name) 
