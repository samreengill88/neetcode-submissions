# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head 

        lst_len = 0

        while curr:
            lst_len += 1
            curr = curr.next
        
        k = lst_len - n

        c = head
        prev = head

        if n == lst_len:
            tmp = c.next 
            c.next = tmp
            c = tmp
            return c
        
        for i in range(k):
            c = c.next
        for i in range(k - 1):
            prev = prev.next

        tmp = c.next 
        prev.next = tmp
        c.next = None

        return head


