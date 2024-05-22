# Input: prices = [7,1,3,5,7,4]
# Output: 7
from typing import List
def maxProfit(prices: List[int]) -> int:
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit        

prices = [7,1,2,5,7,4]
ans = maxProfit(prices)
print(ans)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
    
#         profit = 0
#         min_price = prices[0]
        
#         for price in prices[1:]:
#             if price > min_price:
#                 profit += price - min_price
#             min_price = price
        
#         return profit