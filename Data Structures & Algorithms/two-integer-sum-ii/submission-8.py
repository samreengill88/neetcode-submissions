class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while i < j:
            curr_sum = numbers[i] + numbers[j]
            # curr_sum = 1 + 4 = 5 > target = 3
            #  need to decrease curr_sum so j -= 1
            #           inc: i += 1
            if curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]
        
    # TC: O(n)
    # SC: O(1)