class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int arr[100001] = {0};

        for (int num : nums) {
            if (num >= 0) {
                arr[num]++;
            }
        }

        for (int i = 1; i < 100001; i++) {
            if (arr[i] == 0) {
                return i;
            }
        }
        
    }
};