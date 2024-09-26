// C++ program to check if two strings are anagrams using character counts

#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    // Function to check if two strings are anagrams
    bool isAnagram(string s, string t) {
        // Check if the lengths are different
        if (s.length() != t.length()) {
            return false;
        }

        // Create unordered_maps to store character counts
        unordered_map<char, int> count_s;
        unordered_map<char, int> count_t;

        // Count occurrences of each character in both strings
        for (char char_s : s) {
            count_s[char_s]++;
        }

        for (char char_t : t) {
            count_t[char_t]++;
        }

        // Compare the character counts
        return count_s == count_t;
    }
};

int main() {
    // Example usage
    Solution solution;
    string s = "listen";
    string t = "silent";

    // Check if the strings are anagrams
    if (solution.isAnagram(s, t)) {
        cout << "The strings are anagrams.\n";
    } else {
        cout << "The strings are not anagrams.\n";
    }

    return 0;  // Return 0 to indicate successful execution
}
