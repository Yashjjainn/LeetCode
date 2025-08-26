#leetcode problem : word pattern 
#https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split()
        if len(pattern) != len(string):
            return False
        #this problem is same as the isomorphic string, so here gonna use an alternate method for the same problem
        return len(set(zip(string,pattern))) == len(set(string)) == len(set(pattern))
    ''' the logic here is to create a tuple mapping the pattern and the string using zip(),
    then create a set out of it and compare the size of sets of the mapping and sets of string and pattern,
    cause if there is any pai not following bijective rules it will increase the size of set of mapping'''


#test case 
S = Solution()
pattern = "abba"
s = "dog cat cat fish"
print(S.wordPattern(pattern,s))



