def lettercombination(digits):
    phonedict={
        2:["a","b","c"],
        3:["d","e","f"],
        4:["g","h","i"],
        5:["j","k","l"],
        6:["m","n","o"],
        7:["p","q","r","s"],
        8:["t","u","v"],
        9:["w","x","y","z"]
    }
    dig=list(digits)
    def combine(l):
        if len(dig)>0:
            nl=[]
            numlist=phonedict[int(dig.pop(0))]
            for r in l:
                for c in numlist:
                    nl.append(r+c)
            return combine(nl)
        else:
            return l
        
    return combine(phonedict[int(dig.pop(0))]) if len(dig)>0 else []

print (lettercombination("23"))
print (lettercombination("239"))
print (lettercombination(""))