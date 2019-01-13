def combinationSum(candidates,target):

    def constructDict(candidates,target):
        if target == 0:
            return 0
        
        bottom = True
        for c in candidates:
            if target >= c:
                bottom = False
        
        if not bottom:
            re = {}
            for c in candidates:
                if target >= c:
                    re[c] = constructDict(candidates, target-c)
            return re
        else:
            return None

    dic = constructDict(candidates,target)
   
    #parse dictionary
    def parseDict(dic):
        r = []
        def subParseDict(k,v):
            if not v==None and not v==0:
                listoflist = parseDict(v)
                if not listoflist==None:
                    rl = []
                    for li in listoflist:
                        li.append(k)
                        rl.append(li)
                    return rl
            elif v==0:
                return [[k]]
        
        for k,v in dic.items():
            listoflist = subParseDict(k,v)
            if not listoflist==None: 
                for li in listoflist:
                    r.append(li)
        return r

    if dic==None:
        return []
        
    l = parseDict(dic)
    check = []
    r=[]
    for el in l:
        dic = {}
        for i in el:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        if dic not in check:
            check.append(dic)
            r.append(el)

    return r
     

# candidates = [2,3,6,7]
# target = 7
# print (combinationSum(candidates,target))

# candidates1 = [2,3,5]
# target1 = 8
# print (combinationSum(candidates1,target1))

candidates2 = [2]
target2 = 1
print (combinationSum(candidates2, target2))