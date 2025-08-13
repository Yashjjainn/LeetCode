#leetcode problem: Roman to Integer
#https://leetcode.com/problems/roman-to-integer/solutions/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
        integer = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                integer -= roman[s[i]]
            else:
                integer += roman[s[i]]
        
        integer += roman[s[-1]]
        return integer

#testcase
S = Solution()
a = "CDXLVIII"
print(S.romanToInt(a))