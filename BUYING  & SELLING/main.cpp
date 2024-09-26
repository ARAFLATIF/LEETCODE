#include <iostream>
#include <vector>
#include <algorithm> // For the max function

using namespace std;

class Solution {
public:
    // Function to calculate the maximum profit from stock prices
    int maxProfit(vector<int>& prices) {
        int res = 0;  // Variable to store the maximum profit
        int lowest = prices[0];  // Initialize the lowest price as the first price in the list

        // Iterate through the prices
        for (int price : prices) {
            // Update the lowest price if the current price is lower
            if (price < lowest) {
                lowest = price;
            }
            // Update the maximum profit
            res = max(res, price - lowest);
        }

        return res;  // Return the maximum profit
    }
};

int main() {
    Solution solution;
    vector<int> prices = {7, 1, 5, 3, 6, 4};  // Example prices

    // Calculate and print the maximum profit
    cout << "Maximum Profit: " << solution.maxProfit(prices) << endl;

    return 0;  // R
