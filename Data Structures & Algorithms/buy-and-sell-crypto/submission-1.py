class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = [prices[0]]
        max_profit = 0
        window_max = 0

        for i in range(1, len(prices)):
            if prices[i] < window[0] or i == len(prices) - 1:
                window_max = max(prices[i], window_max)
                profit = window_max - window[0]
                max_profit = max(max_profit, profit)
                window = [prices[i]]
                window_max = prices[i]
            else:
                window.append(prices[i])
                window_max = max(prices[i], window_max)
        return max_profit