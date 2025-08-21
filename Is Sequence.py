#leetcode problem: Is Subsequence
#https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)

#testcase
S = Solution()
s = "abc"
t = "ahbgdc"
print(S.isSubsequence(s,t))