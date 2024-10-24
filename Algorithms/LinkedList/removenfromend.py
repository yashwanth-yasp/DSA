# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    first = head 
    second = head
    for i in range(n):
        second = second.next
    while second.next:
        first = first.next 
        second = second.next
    first.next = first.next.next

    return head


