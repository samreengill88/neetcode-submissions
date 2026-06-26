# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # if lists is empty - return None
        # while you have atleast 1 list in lists:
        #       get consecutive pairs
        #       merge them  (similar to merging 2 sorted lists)
        #       append merged pair to mergedLst
        #       do this until you have list left in mergedLst   

        def merge(l1, l2):
            
            dummy = ListNode()
            curr = dummy
            
            # while l1 and l2 are not empty 
            # get smaller value from l1 or l2 

            while l1 and l2:

                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next
            
            if l1 != None:
                curr.next = l1
            if l2 != None:
                curr.next = l2

            return dummy.next


        if len(lists) == 0:
            return None
        
        while len(lists) > 1:

            mergedLst = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedLst.append(merge(l1, l2))
            
            lists = mergedLst
        
        return lists[0]

        