#leetcode problem : Summary ranges
#https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        Range = []
        start = nums[0]
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i+1] != nums[i] + 1:
                end = nums[i]
                if start == end:
                    Range.append(str(start))
                else:
                    Range.append(f"{start}->{end}")
                start = nums[i+1]
        #handling last range
        if start == nums[-1]:
            Range.append(str(start))
        else:
            Range.append(f"{start}->{nums[-1]}")
        return Range

        
# time = O(n)    space = O(n) cause of output string otherwise O(1)   

#test case 
S = Solution()
s = [1,2,5,6,8,7,8,9]
print(S.summaryRanges(s))