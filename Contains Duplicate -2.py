#leetcode problem : Contains Duplicate 2
#https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        values_seen = {}
        for i in range(len(nums)):
            if nums[i] in values_seen and abs(values_seen[nums[i]] - i) <= k:
                return True
            values_seen[nums[i]] = i
        return False

# time = O(n)      space = O(n)

#test case 
S = Solution()
pattern = [1,5,4,1,2,5,4,6,1,]
s = 3
print(S.containsNearbyDuplicate(pattern,s))