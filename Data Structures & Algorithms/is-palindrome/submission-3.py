class Solution:
    def isPalindrome(self, s: str) -> bool:
        # tab a cat = tacacat
        # have two pointers one(i) at the front of the s and other(j) at the end of s
        # change s to lower case and remove non-alphanumeric characters from s
        # iterate through s until i == j
        # if at any point s[i] != s[j] return False; else increase i by 1 and decrease j by 1

        # remove alpa numeric chars from s 
    #     str = self.removeAlphaNumeric(s).lower()
    #     # print(f"str is {str}")
    #     i = 0
    #     j = len(str) - 1

    #     while (i < j):
    #         if str[i] != str[j]:
    #             return False
    #         else:
    #             i += 1
    #             j -= 1
    #     return True
        
    # def removeAlphaNumeric(self, s):
    #     result = s
    #     for char in s:
    #         if not char.isalnum():  # if character is not alphanumeric i.e. is not a letter or digit
    #             # replace it
    #             result = result.replace(char, '')
    #     return result


        newStr = ''
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        
        return newStr == newStr[::-1]








        