class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertionSort(head):
    if not head:
        return head
    curr=head.next
    sortedhead=head
    sortedtail=head
    head.next=None
    while curr:
        sortedcurr=sortedhead
        if curr.val<=sortedcurr.val:            
            node=curr
            curr=curr.next
            node.next=sortedhead
            sortedhead=node
        else:
            while not sortedcurr.val==sortedtail.val:
                if sortedcurr.next.val>curr.val and sortedcurr.val<=curr.val:
                    node=curr
                    curr=curr.next
                    node.next=sortedcurr.next
                    sortedcurr.next=node
                    break
                else:
                    sortedcurr=sortedcurr.next
            if curr and curr.val>=sortedtail.val:
                node=curr
                curr=curr.next
                sortedtail.next=node
                node.next=None
                sortedtail=node
    return sortedhead

# l1=ListNode(6)
# l2=ListNode(7)
# l3=ListNode(2)
# l4=ListNode(5)
# l5=ListNode(1)
# l6=ListNode(3)
# l7=ListNode(8)
# l1.next=l2
# l2.next=l3
# l3.next=l4
# l4.next=l5
# l5.next=l6
# l6.next=l7
# sorted=insertionSort(l1)
# print (sorted)

# l1=ListNode(4)
# l2=ListNode(2)
# l3=ListNode(1)
# l4=ListNode(3)
# l1.next=l2
# l2.next=l3
# l3.next=l4
# sorted=insertionSort(l1)
# print (sorted) 

# l1=ListNode(1)
# l2=ListNode(1)
# l1.next=l2
# sorted=insertionSort(l1)
# print (sorted) 


l1=ListNode(4)
l2=ListNode(19)
l3=ListNode(14)
l4=ListNode(5)
l5=ListNode(-3)
l6=ListNode(1)
l7=ListNode(8)
l8=ListNode(5)
l9=ListNode(11)
l10=ListNode(15)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
l6.next=l7
l7.next=l8
l8.next=l9
l9.next=l10
sorted=insertionSort(l1)
print (sorted)          