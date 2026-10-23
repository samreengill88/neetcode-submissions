# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. find the middle
        c1 = head
        c2 = head

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next.next
        
        # c1 is at the middle 
        curr = c1.next
        c1.next = None

        # 2. reverse from curr..
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # 3. alternate b/w lists 
        first = head 
        second = prev

        while second:
            f_next = first.next
            s_next = second.next

            first.next = second
            second.next = f_next

            first = f_next
            second = s_next

