class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int largestCount = 0;
        int ans;
        unordered_map<int, int> mp;

        for (int num : nums) {
            mp[num]++;
            if (mp[num] > largestCount) {
                largestCount = mp[num];
                ans = num;
            }
        }

        return ans;
    }
};