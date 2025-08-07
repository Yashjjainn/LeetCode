#Leet Code problem: Remove Duplicates from Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = 1          #Placement Index (since 1st element is always unique)
        for b in range(1,len(nums)):
            if nums[b] != nums[a-1]:
                nums[a] = nums[b]
                a += 1
        return a

#Test Case 
A = [1,3,5,5,5,7,7,7,8,9,9,9]
S = Solution()
print(S.removeDuplicates(A))