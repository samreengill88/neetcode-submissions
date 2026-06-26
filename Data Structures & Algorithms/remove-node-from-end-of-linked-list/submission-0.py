# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # get length of lst 
        i = head 
        lstLen = 0

        while i:
            lstLen += 1
            i = i.next
        
        # k: remove _ element from from 
        k = lstLen - n

        curr = head
        prev = head

         # remove first element
        if n == lstLen:
            tmp = curr.next
            curr.next = None
            curr = tmp
            return curr

        # move curr (k) times and prev (k - 1) times
        for j in range(k):
            curr = curr.next
        for k in range(k - 1):
            prev = prev.next

        # remove kth element
        tmp = curr.next
        prev.next = tmp
        curr.next = None

        return head
        
