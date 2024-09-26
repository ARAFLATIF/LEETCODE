#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    // Function to check if there are duplicates in the array
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;  // Create a set to store seen numbers

        // Iterate through the numbers
        for (int num : nums) {
            // Check if the number has already been seen
            if (seen.find(num) != seen.end()) {
                return true;  // Duplicate found
            }
            seen.insert(num);  // Add the number to the set
        }

        return false;  // No duplicates found
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 1};  // Example input with a duplicate

    // Check for duplicates and print the result
    if (solution.hasDuplicate(nums)) {
        cout << "There are duplicates in the array." << endl;
    } else {
        cout << "No duplicates found in the array." << endl;
    }

    return 0;  // Return 0 to indicate successful execution
}
