class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int size = nums.size() + 2;
        vector<int> arr(size, 0);

        for (int num : nums) {
            if (num >= 0 && num < size) {
                int index = std::min(num,size - 1);
                arr[index] = 1;
            }
        }

        for (int i = 1; i <= size; i++) {
            if (arr[i] == 0) {
                return i;
            }
        }
        
        return -1;
    }
};