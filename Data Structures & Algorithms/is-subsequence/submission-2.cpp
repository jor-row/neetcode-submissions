class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        int tLen = t.length();
        int sLen = s.length();

        while (i < tLen && j < sLen) {
            if (t[i] == s[j]) {
                j++;
            }
            i++;
        }

        return j == sLen;
        
    }
};