class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        preSum = nums[0]
        for i in range(1,len(nums)):
            tempSum=max(preSum, preSum+nums[i],nums[i])
            maxSum=max(tempSum,maxSum)
            if(tempSum==nums[i]):
                preSum=nums[i]
            else:
                preSum+=nums[i]
        if(preSum>maxSum):
            return preSum
        return maxSum