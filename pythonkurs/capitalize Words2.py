
def solve(s): 
    if len(s) > 0 and len(s) < 1000:
        wordlist = s.split()
        for i in range(len(wordlist)):
            if isinstance(wordlist[i][0],str):
                s = s.replace(wordlist[i],wordlist[i].capitalize())
    return s


S =  "aaaa aaaa aaaa oorld  lol"
print(S)
Full_Name=solve(S)
print(Full_Name) 