class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        sum=0
        for i in range(len(seats)):
            sum+=abs(students[i]-seats[i])
        return sum    
        