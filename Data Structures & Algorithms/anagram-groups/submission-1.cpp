class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<unordered_map<char, int>> maps;
        vector<vector<string>> anas;

        for (string str : strs) {
            unordered_map<char, int> mp;
            for (char letter : str) {
                mp[letter]++;
            }
            // check that mp is already in maps
            auto it = find(maps.begin(), maps.end(), mp);

            if (it != maps.end()) {
                // Found
                int index = distance(maps.begin(), it);
                anas[index].push_back(str);
            } else {
                maps.push_back(mp);
                anas.push_back({str});
            }
        }

        return anas;
    }
};
