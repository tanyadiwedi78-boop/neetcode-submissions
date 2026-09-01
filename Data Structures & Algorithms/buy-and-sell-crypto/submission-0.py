class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_prize = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_prize:
                min_prize = price
            elif price - min_prize > max_profit:

                max_profit = price - min_prize
        return max_profit