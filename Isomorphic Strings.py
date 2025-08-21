#leetcode problem: Isomorphic Strings
#https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = dict()
        t_to_s = dict()
        for i in range(len(s)):
            if s[i] in s_to_t and t[i] != s_to_t[s[i]]:  # checking each letter in s is mapped uniquely to one letter in t
                return False
            if t[i] in t_to_s and s[i] != t_to_s[t[i]]:  #checking no two letter in s is mapped to same one letter in t
                return False
            else :
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
        return True
            
        return True

# Time: O(n)
# Space: O(1) since s and t consists only of ASCII (128 characters)



#test case
S = Solution()
s = "egg"
t = "add"
print(S.isIsomorphic(s,t))