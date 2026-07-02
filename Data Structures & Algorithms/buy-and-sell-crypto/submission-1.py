class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, max_profit = 0, 1, 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                if max_profit < profit:
                    max_profit = profit
                s += 1
            else:
                b = s
                s += 1
        
        return max_profit
        