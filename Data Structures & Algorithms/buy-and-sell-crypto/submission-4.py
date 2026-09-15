class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
            
        left = 0
        right = left + 1
        max_profit = 0
        
        # Removed `min_buy` because it was hardcoded to prices[0] and caused the loop bug
        
        while left < len(prices) and right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]
            
            if buy_price < sell_price:
                # Your logic: fast-forward 'right' as long as prices stay high
                while right < len(prices) and prices[right] >= sell_price:
                    profit = prices[right] - buy_price
                    if profit > max_profit:
                        max_profit = profit
                    right += 1
                    
                # FIX 1: Removed `left = right` and `right += 1` from here.
                # If you jump 'left' to 'right' here, you lose the lowest buy_price 
                # you found. We want to keep 'left' exactly where it is so we can 
                # keep testing future peaks against it.
                
            else:
                # FIX 2: Replaced the broken while loop with a simple jump.
                # If buy_price >= sell_price, it means prices[right] is a LOWER price.
                # So we simply move our 'left' pointer to this new, better buy price.
                left = right
                right += 1
                
        return max_profit