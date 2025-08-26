#leetcode problem : Valid Anagram 
#https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
#since this question uses the same logic as Ransome Note problem using an alternative method fot the same here
        count = [0]*26
        for ch1, ch2 in zip(s,t):
            count[ord(ch1)- ord('a')] += 1    # recording frequency of elements in s
            count[ord(ch2)- ord('a')] -= 1    # subtracting frequency of elements in t from frequency of  elements in s
        return all(c == 0 for c in count)   #checking if all the elements in count array are zero after deduction of frequency of t from frequency of s 


#Time = O(n)
#Space = O(1)

#test case 
S = Solution()
a = "listen"
b = "silent"
print(S.isAnagram(b,a))