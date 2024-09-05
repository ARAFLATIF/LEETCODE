# Buy and Sell Crypto
# Solved 
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

SOLUTION : 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


# EXPLANATION OF THE CODE : 

# The class Solution is defined, which contains the method maxProfit.
# The maxProfit method takes a list of stock prices as input and returns the maximum profit possible.
# res = 0 initializes the result (maximum profit) to zero.
# lowest = prices sets the initial lowest price to the first price in the list.
# The code then iterates through each price in the list:
# If the current price is lower than the lowest seen so far, it updates lowest.
# It calculates the potential profit by subtracting the lowest price from the current price.
# The max function compares this potential profit with the current maximum profit (res) and keeps the larger value.
# After checking all prices, the method returns the maximum profit found.
# In simple terms, this algorithm does two things simultaneously as it goes through the prices:
# It keeps track of the lowest price seen so far.
# It calculates the profit if we were to sell at the current price, assuming we bought at the lowest price seen.
# By doing this in a single pass through the prices, it efficiently finds the maximum possible profit without needing to check every possible buy-sell combination.
