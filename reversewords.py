def reverseWords(s):
    l = s.strip(" ").split(" ")
    new = []
    for i in range(0,len(l)):
        new.append(l[len(l)-1-i])
    return " ".join(new)
    


input = "the sky is blue"
print (reverseWords(input))

input1 = "a b "
print (reverseWords(input1))