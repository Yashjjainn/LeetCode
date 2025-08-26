#leetcode problem : Two Sum
#https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        values_seen = {}                     # to remember the values we have iterated so far
        for i in range(len(nums)):
            complement = target - nums[i]     #calculating complement for each value in nums
            if complement in values_seen:      # checking if we have iterated over required complement
                return [values_seen[complement],i]
            values_seen[nums[i]] = i
        

# time = O(n)
# space = O(n) 

#test case 
S = Solution()
nums = [2,7,11,15]
target = 9
print(S.twoSum(nums,target))