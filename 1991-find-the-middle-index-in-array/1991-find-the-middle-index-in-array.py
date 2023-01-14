class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums.count(0)==2:
                return 0
            elif nums[0]==0:
                return 1
            elif nums[1]==0:
                return 0
            
            return -1
            
        else:
            i=0  
            while i!=len(nums):
                if i==0:                    
                    right = nums[i+1:]
                    if sum(right)==0:
                        return i
                
                elif i==len(nums)-1:
                    print(i,nums[:i])
                    left = nums[:i]
                    if sum(left)==0:
                        return i
                    
                else:                    
                    left = nums[:i]
                    right = nums[i+1:]
                    if sum(left)==sum(right):
                        return i
                i+=1
                print(i)
                
            return -1
        