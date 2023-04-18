class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def fact(n):
            if n==0 or n==1:
                return 1
            
            else:
                return n*fact(n-1)
            
        
        count = 0
        e = fact(n)
        while e%10==0:
            count+=1
            e//=10
            
        return count
            
        