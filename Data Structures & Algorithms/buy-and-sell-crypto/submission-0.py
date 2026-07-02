class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for b in range(len(prices) - 1):
            for s in range(b + 1, len(prices)):
                profit = prices[s] - prices[b]

                if profit > max_profit:
                    max_profit = profit
        

        return max_profit
        