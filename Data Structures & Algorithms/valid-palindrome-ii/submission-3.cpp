class Solution {
public:
    bool validPalindrome(string s, int maxSkip = 1) {
        int skipped = 0;
        int l = 0;
        int r = s.length() - 1;

        cout << s << "\n";

        while (l < r) {
            if (s[l] != s[r]) {
                if (skipped < maxSkip) {
                    return validPalindrome(s.substr(0, l) + s.substr(l + 1), 0) || validPalindrome(s.substr(0, r) + s.substr(r + 1), 0);

                    skipped++;
                } else {
                    return false;
                }
            } else {
                l++;
                r--;
            }
        }

        return true;

        
    }
};