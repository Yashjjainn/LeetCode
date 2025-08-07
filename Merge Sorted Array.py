# LeetCode Problem: Merge Sorted Array
#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        a = m-1   # last index of meaningful nums1
        b = n-1   # last index of nums2
        c = m+n-1 # placement pointer
        while b >= 0:
            if a >= 0 and nums1[a]>nums2[b] :
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1

# Test Case

S = Solution()
a = [1,3,5,7,8,10,0,0,0]
m = 6
b = [1,5,8]
n = 3

S.merge(a,m,b,n)
print(a)