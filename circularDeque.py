class CircularDeque:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.__size=k
        self.__data=[]

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.__data)==self.__size:
            return False
        else:
            self.__data.insert(0,value)
            return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.__data)==self.__size:
            return False
        else:
            self.__data.insert(self.__size-1,value)
            return True 

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.__data:
            return False
        else:
            self.__data.pop(0)
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.__data:
            return False
        else:
            self.__data.pop()
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.__data:
            return -1
        else:
            return self.__data[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.__data:
            return -1
        else:
            return self.__data[len(self.__data)-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.__data==[]

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return len(self.__data)==self.__size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

c = CircularDeque(3)
print (c.insertLast(1))			
print (c.insertLast(2))			
print (c.insertFront(3))			
print (c.insertFront(4))			
print (c.getRear())  			
print (c.isFull())				
print (c.deleteLast())		
print (c.insertFront(4))			
print (c.getFront())
print (c)			