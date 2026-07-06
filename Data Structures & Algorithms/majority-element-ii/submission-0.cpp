class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;

        for (int num : nums) {
            mp[num]++;
        }

        vector<int> res;

        for (auto key : mp) {
            if (mp[key.first] > nums.size() / 3) {
                res.push_back(key.first);
            }
        }

        return res;
        
    }
};