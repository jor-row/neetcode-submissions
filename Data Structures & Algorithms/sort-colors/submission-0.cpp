class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = 0;

        while (i < nums.size() - 1) {
            if (nums[i] > nums[i+1]) {
                int dummy = nums[i+1];
                nums[i+1] = nums[i];
                nums[i] = dummy;
                i = 0;
            } else {
                i++;
            }
        }
        
    }
};