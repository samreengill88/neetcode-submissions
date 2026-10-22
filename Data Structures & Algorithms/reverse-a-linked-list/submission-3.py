# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        prev = None

        while curr:
            tmp = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    # TC: O(n) -> while loop visits each node once
    # SC: O(1) -> no new nodes created