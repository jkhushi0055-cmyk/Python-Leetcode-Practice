class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        a=0
        altitute=[0]
        for i in range(len(gain)):
            a=a+gain[i]
            altitute.append(a)
        maximum=max(altitute)
        return maximum        


        