class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProfit = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            } else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}


//EXPLANATION : 

// The class Solution is defined with the method maxProfit.
// The method takes an array of stock prices as input and returns the maximum profit possible.
// Three variables are initialized:
// left: represents the buying day, starting at index 0
// right: represents the selling day, starting at index 1
// maxProfit: keeps track of the maximum profit, initially set to 0
// The code uses a while loop that continues as long as right is less than the length of the prices array.
// Inside the loop:
// If the price at right is higher than the price at left, it calculates the profit and updates maxProfit if this profit is higher.
// If the price at right is lower than or equal to the price at left, it moves left to right. This is because we've found a new potential buying day with a lower price.
// right is incremented in each iteration to move to the next day.
// After the loop ends, the method returns the maximum profit found.
// In simpler terms, this algorithm:
// Uses two pointers: one for the buying day and one for the selling day.
// Moves the "selling day" pointer forward each day.
// If it finds a profit, it compares it with the max profit so far.
// If it finds a lower buying price, it moves the "buying day" pointer to that day.
// This approach also efficiently solves the problem in a single pass through the prices,
//   but it does so by always keeping track of a potential buying day and checking each subsequent day as a potential selling day.
