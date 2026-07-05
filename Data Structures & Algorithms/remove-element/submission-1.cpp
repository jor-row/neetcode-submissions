class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int i = 0;

        while (i < nums.size() - count) {
            if (nums[i] == val) {
                for (int j = i; j < nums.size() - 1; j++) {
                    int dummy = nums[j+1];
                    nums[j+1] = val;
                    nums[j] = dummy;
                }
                count++;
            } else {
                i++;
            }

            cout << "[";
            for (int num : nums) {
                cout << num << ",";
            }
            cout << "]";
            cout << "\n";
        }
        
        return nums.size() - count;
    }
};