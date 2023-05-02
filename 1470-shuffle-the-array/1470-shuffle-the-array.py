class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        e = []
        i=0
        j=len(nums)//2
        
        while j!=len(nums):
            e.extend([nums[i],nums[j]])
            i+=1
            j+=1
            
        return e