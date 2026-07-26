class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        hs = sorted(heights, reverse=True)
        hs_i = [heights.index(num) for num in hs]


        print(hs)
        print(hs_i)


        return [names[i] for i in hs_i]
        