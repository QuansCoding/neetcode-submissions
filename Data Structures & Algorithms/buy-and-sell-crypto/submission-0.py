class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:  # iterates through each price in prices
            maxP = max(maxP, sell - minBuy)  #check maxP with previous 
            minBuy = min(minBuy, sell)

        return maxP