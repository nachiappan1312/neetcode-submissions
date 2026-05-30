class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        res = [1]*numsLength
        for i in range(1, numsLength):
            res[i] = res[i-1]*nums[i-1]
        right = 1
        for i in range(numsLength-2, -1, -1):
            right *= nums[i+1]
            res[i]*=right
        return res       