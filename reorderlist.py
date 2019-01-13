def reorderList(head):
    def gettail(head):
        curr=head
        while curr.next.next:
            curr=curr.next
        tail = curr.next
        curr.next=None
        return tail
    
    curr=head
    while curr.next:
        nextNode=curr.next
        if nextNode.next:
            curr.next = gettail(curr)
            curr.next.next=nextNode
            curr=nextNode
        else:
            curr=nextNode

    #print
    curr=head
    while curr:
        print (str(curr.val) + "--->")
        curr=curr.next

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

    def setNext(self, node):
        self.next=node

# n1 = ListNode(3)
# n2 = ListNode(5)
# n3 = ListNode(8)
# n4 = ListNode(10)
# n5 = ListNode(13)

# n1.setNext(n2)
# n2.setNext(n3)
# n3.setNext(n4)
# n4.setNext(n5)

# reorderList(n1)
#############
n1 = ListNode(3)
n2 = ListNode(5)
n3 = ListNode(8)
n4 = ListNode(10)
n5 = ListNode(15)
n6 = ListNode(16)
n7 = ListNode(19)
n8 = ListNode(23)
n9 = ListNode(24) 
n10 = ListNode(27)
n11 = ListNode(30)
n12 = ListNode(33)

n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)
n4.setNext(n5)
n5.setNext(n6)
n6.setNext(n7)
n7.setNext(n8)
n8.setNext(n9)
n9.setNext(n10)
n10.setNext(n11)
n11.setNext(n12)

reorderList(n1)