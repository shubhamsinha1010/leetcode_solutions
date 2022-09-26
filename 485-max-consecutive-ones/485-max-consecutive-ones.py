class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count=0
        t = 0
        for i in nums:
            
            if i==1:
                count+=1
            else:
                t = max(t,count)   
                count=0
        if t<count:
            return count
                
        return t
                