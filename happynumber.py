def isHappy(num):
    def add(n):
        digits=list(str(n))
        sum=0
        for d in digits:
            sum+=int(d)**2
        return sum

    seen=[num]
    re=add(num)
    seen.append(re)
    while True:
        re=add(re)
        if re==1:
            return True
        if re in seen:       
            return False
        seen.append(re)          

print (isHappy(2))