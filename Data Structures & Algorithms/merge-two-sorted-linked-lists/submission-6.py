# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # mergedLst = ListNode()
        # both lists are sorted
        # until both lists are not null
        #   get min val of list1 or list2 - add it to mergedLst
        # when one of the list is empty - add all other remaining elements of other lst to mergedLst 

        mergedLst = ListNode()
        curr = mergedLst

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # if one of the list is not empty
        if list1 != None:
            curr.next = list1
        if list2 != None:
            curr.next = list2
        
        return mergedLst.next