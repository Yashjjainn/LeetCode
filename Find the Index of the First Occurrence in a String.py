#leetcode problem: Find the Index of the First Occurrence in a String
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k, s = len(needle), len(haystack)
        for i in range(s-k+1):
            if needle == haystack[i:i+k]:
                return i
        return -1


# Test case
S = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(S.strStr(haystack,needle))