#leetcode problem: length of last word
#https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = len(s)-1
        length = 0
        while x >= 0 and s[x] == " ":
            x -= 1
        while x >= 0 and s[x] != " ":
            length += 1
            x -= 1
        return length

#testcase
S = Solution()
a = "   fly me   to   the moon  "
print(S.lengthOfLastWord(a))

