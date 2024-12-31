BestTimeToBuyAndSellAStock(optimized).py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-mini
            maxi=max(maxi,profit)
            mini=min(mini,prices[i])
        return maxi
