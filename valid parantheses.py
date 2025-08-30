#leetcode problem : Valid parantheses
#https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')', '{':'}', '[':']'}   #opening -> closing
        for ch in s:
            if ch in mapping:             #opening bracket encountered
                stack.append(mapping[ch])     #push corresponding closing bracket in stack
            else:                       #closing bracket encountered
                top = stack.pop() if stack else "#"      
                if ch != top:              #check if correct closing
                    return False 
        return not stack        #stack must be empty to ensure all brackets closed

# time:O(n)         Space: O(n) 

#test case 
S = Solution()
s = "(){}{]{){]}}}"
print(S.isValid(s))