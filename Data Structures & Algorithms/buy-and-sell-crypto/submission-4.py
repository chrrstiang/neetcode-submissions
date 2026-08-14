class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        window_max = prices[0]
        window_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < window_min or i == len(prices) - 1:
                window_max = max(prices[i], window_max)
                profit = window_max - window_min
                max_profit = max(max_profit, profit)
                window_max = prices[i]
                window_min = prices[i]
            else:
                window_max = max(prices[i], window_max)
        return max_profit