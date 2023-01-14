class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = []
        t = 0
        for i in range(len(gain)):
            t+=gain[i]
            s.append(t)
            
        return max(s) if max(s)>0 else 0
            
        