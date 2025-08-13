#Leetcode Problem : Best time to but & sell stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        maxprofit = 0
        for price in prices:
            if price < buy:
                buy = price # update buying rice
            profit = price - buy
            if profit > maxprofit:
                maxprofit = profit
        return maxprofit

#testcase 
S = Solution()
A = [2,4,1,2]
print(S.maxProfit(A))
