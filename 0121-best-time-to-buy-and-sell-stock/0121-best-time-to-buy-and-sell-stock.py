class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low=prices[0]
        profit=0
        for i in prices:
            if i<low:
                low=i
            if i-low>profit:
                profit=i-low
        return profit