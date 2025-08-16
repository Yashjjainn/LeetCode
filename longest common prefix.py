#leetcode problem: Longest Common Prefix 
#https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != prefix:
                    return strs[0][:i]
        return strs[0]

#testcase 
S = Solution()
a = ["flower","flow","flight"]
print(S.longestCommonPrefix(a))