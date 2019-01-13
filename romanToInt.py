def romanToInt(s):
    l = list(s)
    v = 0
    print (l)
    for i in range(0,len(l)):
        if (l[i]=="I"):
            if (i<len(l)-1):
                if (l[i+1] == "V" or l[i+1] == "X"):
                    v-=1
                else:
                    v+=1
            else:
                v+=1

        if (l[i] == "V"):
            v+=5
        if (l[i] == "X"):
            if (i<len(l)-1):
                if (l[i+1] == "L" or l[i+1] == "C"):
                    v-=10
                else:
                    v+=10
            else:
                v+=10

        if (l[i] == "L"):
            v+=50

        if (l[i] == "C"):
            if (i<len(l)-1):
                if (l[i+1] == "D" or l[i+1] == "M"):
                    v-=100
                else:
                    v+=100
            else:
                v+=100

        if (l[i] == "D"):
            v+=500
        
        if (l[i] == "M"):
            v+= 1000

    return v

print (romanToInt("III"))
print (romanToInt("MCMXCIV"))
print (romanToInt("DCXXI"))