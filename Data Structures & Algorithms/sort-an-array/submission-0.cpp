class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int i = 0;
        int cnt = 0;

        while (i < nums.size() - cnt - 1) {
            int j = i;
            if (nums[i] > nums[i+1]) {
                while (j < nums.size() - cnt - 1 && nums[j] > nums[j+1]) {
                        int dummy = nums[j+1];
                        nums[j+1] = nums[j];
                        nums[j] = dummy;
                        j++;
                }
                i = 0;
            } else {
                i++;
            }
        }
        return nums;
    }
};