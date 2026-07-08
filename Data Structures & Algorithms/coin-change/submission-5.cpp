class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        unordered_map<int, int> mp;

        std::function<int(int)> dfs = [&](int amount) {
            if (mp.find(amount) != mp.end()) {
                return mp[amount];
            } else if (amount == 0) {
                return 0;
            }

            int res = 1e9;
            for (int coin : coins) {
                if (amount - coin >= 0) {
                    res = std::min(1 + dfs(amount - coin), res);
                }
            }
            mp[amount] = res;
            return res;
        };

        int minCoinCount = dfs(amount);

        if (minCoinCount < 1e9) {
            return minCoinCount;
        } else {
            return -1;
        }
        
    }
};