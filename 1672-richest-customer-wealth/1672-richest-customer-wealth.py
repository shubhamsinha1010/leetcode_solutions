class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = 0
        for i in accounts:
            e = sum(i)
            r = max(r,e)
            
        return r
            
        