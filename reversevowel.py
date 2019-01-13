def reverseVowel(s):
    # slist=list(s)
    # vowels=["a","e","i","o","u","A","E","I","O","U"]
    # if s=="":
    #     return ""
    # front=0
    # end=-1
    # while front<len(slist) and slist[front] not in vowels:
    #     front+=1
    # while -end<len(slist) and slist[end] not in vowels:
    #     end-=1

    # while front<len(slist)+end:
    #     tmp=slist[front]
    #     slist[front]=slist[end]
    #     slist[end]=tmp
    #     front+=1
    #     end-=1
    #     while front<len(slist) and slist[front] not in vowels:
    #         front+=1
    #     while -end<len(slist) and slist[end] not in vowels:
    #         end-=1

    # return "".join(slist)
    
    newstr=s
    newlist=[]
    st=""
    for i in s:
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            newstr=newstr.replace(i,"*")
            newlist.append(i)
        p=len(newstr)
        l=len(newlist)
        m=l
    for t in newstr:
        if t=="*":
            m-=1
            if m>=0:
                st+=newlist[m]
        else:
            st+=t
    return st

print (reverseVowel("0P"))