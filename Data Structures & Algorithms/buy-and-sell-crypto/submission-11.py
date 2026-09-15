class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We keep a left pointer which tracks what we would buy a stock at
        # We have a right which represents when we would sell a stock
        # We see current profit status
        # If left pointer greater, we increment left since we want to buy at cheaper price
        # if right pointer greater or equal, We increment right until it keeps increasing, updating max profit found
        # once a decrease is found we stop
        # we move left to right, and right to left + 1
        # then we repeat


        # Lets say array size of 2
        # if the array is [10, 1] we increase left to 1 and then compare prices, see that equal, increment right until end, end is found, and then return the profit which is 0

        # For array of size 1 profit is just 0
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

