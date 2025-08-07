#Leet Code Problem: Majority Element
#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

'''using moore's voting algo without second step of verifying the candidate.
since we have assumed majority always exist'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0
        candidate = None 
        for i in nums:
            if vote == 0:
                candidate = i
            vote += (1 if i == candidate else -1)
        return candidate

#Test Case 
S = Solution()
A = [1,3,2,3,5,3,4,5,3,6,3,3,3]
print(S.majorityElement(A))