class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        vis=""
        for i in key:
            if i !=" " and i not in vis:
                vis+=i
        ans=""
        for i in message:
            if i in vis:
                ans+=alpha[vis.index(i)]
            else:
                ans+=i    
        return ans                
        