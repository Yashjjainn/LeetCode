#leetcode Problem : Ransomn Note
#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = dict()
        magazine_count = dict()
        
        for ch in ransomNote:                          # Counting letters in ransomNote
            ransom_count[ch] = ransom_count.get(ch,0) + 1
        for m in magazine:                                # Counting letters in magazine
            magazine_count[m] = magazine_count.get(m,0) + 1

        for letter, frequency in ransom_count.items():     # checking if magazine has enough of each letter of ransomNote
            if magazine_count.get(letter,0) < frequency:
                return False
        return True

#Test case
S = Solution()
m = "dszhbhcvchdsfvvhjadf"
r = "dfdfhbjvjdkfd"
print(S.canConstruct(r,m))