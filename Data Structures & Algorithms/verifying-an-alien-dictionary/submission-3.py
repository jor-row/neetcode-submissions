class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        nums = []
        longest = 0

        for word in words:
            nums.append([])
            for char in word:
                num = order.index(char)
                nums[-1].append(num)
            longest = max(longest, len(word))

        print(nums)

        # go through them two by two, confirming they are in the correct order

        for i in range(len(nums) - 1):
            a = nums[i]
            b = nums[i+1]
            print(a)
            print(b)
            l = min(len(a), len(b))
            in_order = True
            non_equal = False
            for j in range(l):
                if a[j] > b[j]:
                    return False
                if a[j] < b[j]:
                    non_equal = True
                    break

            if non_equal is False and len(a) > len(b):
                return False

        return True
                


        