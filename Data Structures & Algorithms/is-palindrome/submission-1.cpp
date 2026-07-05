#include <vector>

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> letters;

        for (char letter : s) {
            if (std::isalnum(letter)) {
                letters.push_back(std::tolower(letter));
            }
        }
        
        int i = 0;
        int j = letters.size() - 1;

        while (i < j) {
            if (letters[i] != letters[j]) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};
