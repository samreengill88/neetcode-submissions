# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # two pointers c1 and c2
        # c1 moves one step
        # c2 moves 2 steps
        # if there is a cycle eventually c1 == c2

        c1 = head
        c2 = head

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next.next
            
            if c1 == c2:
                return True
            
            
        
        return False
