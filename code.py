class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]==1:
                c+=1
            elif nums[i]%3==1:
                c+=1
            elif nums[i]%3==2:
                c+=1
        return c
            
        
