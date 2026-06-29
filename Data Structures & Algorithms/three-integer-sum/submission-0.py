class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        prev_numi = None

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            if nums[i] > 0:
                break

            if nums[i] == prev_numi:
                continue

            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    prev_numi = nums[i]
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1

        return ans





        