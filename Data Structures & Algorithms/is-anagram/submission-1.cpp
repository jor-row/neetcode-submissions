#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> smp;
        unordered_map<char, int> tmp;

        for (char sub_s : s) {
            smp[sub_s]++;
        }

        for (char sub_t : t) {
            tmp[sub_t]++;
        }

        if (smp == tmp) {
            return true;
        }

        return false;
        
    }
};
