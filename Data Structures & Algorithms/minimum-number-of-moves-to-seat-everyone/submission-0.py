class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()


        difference = 0

        for i in range(len(seats)):
            difference += abs(seats[i] - students[i])

        return difference
        