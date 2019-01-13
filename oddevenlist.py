def oddEvenList(head):
    curr=head
    while curr.next.next:
        oddnode=curr.next.next
        evennode=curr.next
        curr.next=oddnode
        oddnode.next=evennode
        curr=evennode
    


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
ret = oddEvenList(l1)
print(ret)
