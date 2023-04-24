class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftarr = [0]
        tsum = 0
        for i in range(len(nums)-1):
            tsum+=nums[i]
            leftarr.append(tsum)
            
        rightarr=[0]*len(nums)
        sums=0
        
        for i in range(len(nums)-1,0,-1):
            sums+=nums[i]
            rightarr[i-1]=sums
            
        fin_arr = [0]*len(nums)
        for i in range(len(nums)):
            fin_arr[i]=abs(leftarr[i]-rightarr[i])
            
        return fin_arr
            
            
        
            
            