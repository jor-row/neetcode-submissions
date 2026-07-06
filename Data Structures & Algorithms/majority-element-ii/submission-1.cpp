class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;

        for (int num : nums) {
            mp[num]++;
        }

        vector<int> res;

        for (auto& pair : mp) {
            if (pair.second > nums.size() / 3) {
                res.push_back(pair.first);
            }
        }

        return res;
        
    }
};