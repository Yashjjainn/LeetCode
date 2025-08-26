#leetcode problem : Happy number
#https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isHappy(self, n: int) -> bool:
        values_seen = set()       # for remembering the values of n so far
        while n != 1 and n not in values_seen:  #only two possible situations for n either it reaches one or it loops back
            values_seen.add(n)
            n = sum(int(digit)**2 for digit in str(n)) #calculating square sum of digits

        return n == 1


# time = O(logn)    Space = O(logn)



#test case 
S = Solution()
n = 33
print(S.isHappy(n))