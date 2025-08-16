#leetcode problem : Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

#test case
S = Solution()
a = "A man, a plan, a canal: Panama"
print(S.isPalindrome(a))