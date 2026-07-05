class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string longestPrefix = "";

        if (strs.size() == 1) {
            return strs[0];
        }

        int endIndex = 0;

        while (true) {
            if (strs[0].size() < endIndex + 1) {
                return longestPrefix;
            }

            char lastChar = strs[0][endIndex];

            for (string str : strs) {
                if (str.size() < endIndex + 1 || str[endIndex] != lastChar) {
                    return longestPrefix;
                }
            }
            endIndex++;
            longestPrefix += lastChar;
        }



        
    }
};