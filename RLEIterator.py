class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.__seq={}
        while A:
            try:
                num=A.pop(1)
                rep=A.pop(0)
            except IndexError:
                break
            self.__seq[rep]=num


    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>len(self.__seq):
            self.__seq=[]
            return -1
        else: 
            re=self.__seq[n-1]
            self.__seq=self.__seq[n:]
            return re

A=[3,8,0,9,2,5]
obj=RLEIterator(A)
print (obj.next(2))
print (obj.next(1))
print (obj.next(1))
print (obj.next(2))