class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        right = left + 1
        max_profit = 0
        while right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]
            if buy_price < sell_price:
                while right < len(prices) and prices[right] >= sell_price:
                    profit = prices[right] - buy_price
                    if profit > max_profit:
                        max_profit = profit
                    right += 1
            else:
                left = right
                right += 1
        return max_profit

