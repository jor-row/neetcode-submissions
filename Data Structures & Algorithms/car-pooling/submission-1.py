class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        kms = [0 for i in range(1001)]

        for trip in trips:
            kms[trip[1]] += trip[0]
            kms[trip[2]] -= trip[0]


        running_cap = capacity

        for km in kms:
            running_cap -= km

            if running_cap > capacity or running_cap < 0:
                return False

        return True 