# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        c1 = head
        c2 = head 

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next.next

            # there is a cycle 
            if c1 == c2: 
                return True
        return False
    
    # TC: O(n)
    # SC: O(1)