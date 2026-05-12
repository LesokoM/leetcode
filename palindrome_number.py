"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

palindrome: An integer is a palindrome when it reads the same forward and backward.
"""




class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reversed = str(x)[::-1]
        x_original = str(x)[:]
        palindrome = True
        for i in range(0,len(x_original)):
            if x_original[i] == x_reversed[i]:
                pass
            else:
                return False
    
        return palindrome

    
sol = Solution()
print(sol.isPalindrome(-121))