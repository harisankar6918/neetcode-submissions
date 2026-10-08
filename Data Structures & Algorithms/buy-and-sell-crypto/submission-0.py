class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d=0
        md=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                d=prices[j]-prices[i]
                print(d)
                md=max(md,d)
        return md