# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get kth node 
        def getKthNode(curr, k):
            while curr and k > 0:
                k -= 1
                curr = curr.next
               
                
            return curr
        
        # create dummy node and point it to head
        dummy = ListNode()
        dummy.next = head
        before_group = dummy

        while True:

            # check if we have k nodes remaining
            kth_node = getKthNode(before_group, k)
            if not kth_node:
                break
            
            # save the node after the group
            group_next = kth_node.next


            # reverse the group
            prev, curr = group_next, before_group.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # connect to previous group
            tail = before_group.next
            before_group .next = kth_node
            before_group = tail
        
        return dummy.next

            




        
