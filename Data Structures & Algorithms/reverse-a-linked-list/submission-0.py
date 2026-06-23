# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head 

        # Input: Null -> 1 -> 2 -> 3 -> 4
        # Output: Null <- 1


        while curr is not None:
            next_val = curr.next
            curr.next = prev
            prev = curr # prev is 1 
            curr = next_val
        
        return prev 

        