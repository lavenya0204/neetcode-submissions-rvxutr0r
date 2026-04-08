class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=len(set(nums))
        n=len(nums)
        if(n>s):
            return True
        else:
            return False