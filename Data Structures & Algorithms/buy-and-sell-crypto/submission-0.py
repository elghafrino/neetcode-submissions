class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = prices[0]
        m = 0
        for i in range(len(prices)):
            if prices[i] < s:
                s = prices[i]
            elif prices[i] - s> m:
                m = prices[i] - s
        return m


