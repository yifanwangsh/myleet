def intToRoman(num):
    l = list(str(num))
    dic = {}
    for i in range(0,len(l)):
        dic[len(l)-i-1] = l[i]

    r = ""
    for k,v in dic.items():
        vint = int(v)

        if (vint >= 0 and vint <=3):
            if (k==0):
                r += "I"*vint
            elif (k==1):
                r+= "X"*vint
            elif (k==2):
                r+= "C"*vint
            elif (k==3):
                r+= "M"*vint
        elif (vint == 4):
            if (k==0):
                r += "IV"
            if (k==1):
                r += "XL"
            elif (k==2):
                r += "CD"
        elif (vint >= 5 and vint <= 8):
            if (k==0):
                r += "V" + "I"*(vint-5)
            elif (k==1):
                r += "L" + "X"*(vint-5)
            elif (k==2):
                r += "D" + "C"*(vint-5)
        else:
            if (k==0):
                r += "IX"
            elif (k==1):
                r += "XC"
            elif (k==2):
                r += "CM"
    
    return r


print (intToRoman(58))
print (intToRoman(1994))