import unittest
def twoSum(numbers,target):
    dic={}
    index1 = -1
    index2 = -1
    for i in range(0,len(numbers)):
        if numbers[i] in dic.keys():
            index1 = dic[numbers[i]]
            index2 = i
            break
        else:
            dic[target-numbers[i]] = i
    return [index1+1,index2+1]


class TestMethod(unittest.TestCase):
    def test1(self):
        numbers=[2,7,11,15]
        target=9 
        self.assertEqual([1,2],twoSum(numbers,target))

    def test2(self):
        numbers=[3,5,11,15,18,23]
        target=20 
        self.assertEqual([2,4],twoSum(numbers,target))    
    

unittest.main()