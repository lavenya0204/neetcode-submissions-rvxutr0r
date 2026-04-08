class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[1]*n
        for i in range(1,n):
            r[i]=r[i-1]*nums[i-1]
        postf=1
        for i in range(n-1,-1,-1):
            r[i]*=postf
            postf*=nums[i]
        return r 

        