class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        max_distance=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i]!=colors[j]:
                    sub=abs(i-j)
                    max_distance=max(max_distance,sub)
        return max_distance            
        