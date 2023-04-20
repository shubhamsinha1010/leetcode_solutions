class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count=0
        while n>0:
            count+=1
            n-=count
            if n<count+1:
                return count
            
        return count
            