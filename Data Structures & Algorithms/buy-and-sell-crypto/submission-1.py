class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprice=0
        for i in range(1,len(prices)):
            price=prices[i]-minprice
            maxprice=max(maxprice,price)
            minprice=min(minprice,prices[i])
        return maxprice