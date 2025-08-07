#Leet Code Problem: Remove Element
#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        a = 0
        for b in range(len(nums)):
            if nums[b] != val:
                nums[a] = nums[b]
                a += 1
        return a

#Test Case 
A = [2,4,3,2,5,7,4,6,7,7,9]
v = 7
S = Solution()
print(S.removeElement(A,v))

