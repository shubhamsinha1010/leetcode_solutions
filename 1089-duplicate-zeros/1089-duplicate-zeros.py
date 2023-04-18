class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        while i<len(arr)-1:
            if arr[i]==0:
                arr.insert(i+1,0)
                i+=2
                del arr[len(arr)-1]
                
            else:
                i+=1
        
        