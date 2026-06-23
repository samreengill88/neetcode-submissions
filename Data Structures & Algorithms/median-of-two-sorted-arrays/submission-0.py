class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use merge of mergeSort to merge nums1 and nums2
        # check if len of final lst is odd, then median is n // 2 th element 
        #                           is even, then median is average of 2 middle elements

        def merge(nums1: list[int], nums2: list[int]):
            index1 = 0
            index2 = 0
            merged = []

            while index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] < nums2[index2]:
                    merged.append(nums1[index1])
                    index1 += 1
                else:
                    merged.append(nums2[index2])
                    index2 += 1
            if index1 < len(nums1):
                merged.extend(nums1[index1:])
            else:
                merged.extend(nums2[index2:])
            return merged
        
        merged_lst = merge(nums1, nums2)
        # print(f"merged_lst is {merged_lst}")
        median = 0
        n = len(merged_lst)
        mid = n // 2
        if len(merged_lst) % 2 == 0:  # len of lst is even
            # print(f"middle element is {merged_lst[mid]}")
            # print(f"middle element - 1 is {merged_lst[mid - 1]}")

            median = (merged_lst[mid] + merged_lst[mid-1]) / 2.0
        else:
            median = merged_lst[n // 2] / 1.0

        return median
