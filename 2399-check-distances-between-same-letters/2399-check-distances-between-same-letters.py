class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        a=len(s)
        for i in range(a):
            for j in range(i+1,a):
                if s[i]==s[j]:
                    dis=j-i-1
        
                    if dis!=distance[ord(s[i])-ord("a")]:
                        return False
        return True        

        