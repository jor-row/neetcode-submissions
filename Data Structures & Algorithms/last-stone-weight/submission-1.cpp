class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // First, sort stones

        int i = 0;
        while (i < stones.size() - 1) {
            if (stones[i] > stones[i+1]) {
                int dummy = stones[i+1];
                stones[i+1] = stones[i];
                stones[i] = dummy;
                i = 0;
            } else {
                i++;
            }
        }

        // Now we can just choose the last 2 elements

        while (stones.size() >= 1) {
            cout << stones.size() << "\n";
            if (stones.size() == 1) {
                cout << "size 1" << "\n";
                return stones[0];
            }

            int finalIndex = stones.size() - 1;

            if (stones[finalIndex] > stones[finalIndex - 1]) {
                int newWeight = stones[finalIndex] - stones[finalIndex - 1];
                stones[finalIndex] = newWeight;
                stones.erase(stones.begin() + finalIndex - 1);
            } else if (stones[finalIndex] < stones[finalIndex - 1]) {
                int newWeight = stones[finalIndex - 1] - stones[finalIndex];
                stones[finalIndex - 1] = newWeight;
                stones.erase(stones.begin() + finalIndex);
            } else {
                stones.erase(stones.begin() + finalIndex);
                stones.erase(stones.begin() + finalIndex - 1);
            }

            int j = 0;
            while (stones.size() > 0 && j < stones.size() - 1) {
                if (stones[j] > stones[j+1]) {
                    int dummy = stones[j+1];
                    stones[j+1] = stones[j];
                    stones[j] = dummy;
                    j = 0;
                } else {
                    j++;
                }
            }

            cout << "[";
            for (int num : stones) {
                cout << num << ", ";
            }
            cout << "]" << "\n";

        }

        return 0;
    }
};
