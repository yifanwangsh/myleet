def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    s = strs.pop(0)
    prefixes = []
    for i in range(0, len(s)):
        prefixes.append(s[:i+1])
    
    check = prefixes.copy()

    for s in strs:
        for p in check:
            if (not s.find(p) == 0 and p in prefixes):
                prefixes.remove(p)
    
    if (len(prefixes) > 0):
        return prefixes[len(prefixes)-1]
    else:
        return ""

l = ["flower", "flow", "flight"]
print (longestCommonPrefix(l))
