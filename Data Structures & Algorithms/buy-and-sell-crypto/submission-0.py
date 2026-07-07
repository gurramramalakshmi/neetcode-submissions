class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        m = 0
        for i in range(1,len(prices)):
            if prices[i]< low:
                low  = prices[i]
            else:
                m = max(m,prices[i]-low)
        return m

        