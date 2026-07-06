# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle of the LL
        #  reverse the second half
        # alternate bw both lists

        c1 = head
        c2 = head

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next.next
        
        # now c1 is at the middle 

        # reverse the second half
        curr = c1.next
        
        c1.next = None
        

        
        prev = None

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        # alternate between the lists 
        # starting of reverse lst is at prev
        
        c = head

        while prev:
            tmp = c. next
            tmp2 = prev.next
            c.next = prev
            prev.next = tmp
            c = tmp 
            prev = tmp2
        

