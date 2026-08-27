class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        prefix=[1]
        for i in range(1,len(nums)):
            prefix.append(nums[i-1]*prefix[i-1])
        suffix=1
        for j in range(len(nums)-1,-1,-1):
            r[j]=suffix*prefix[j]
            suffix*=nums[j]
        return r


            

            
