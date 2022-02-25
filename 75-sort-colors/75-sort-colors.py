class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if(nums[j]<1):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        j=len(nums)-1
        while(i<j):
            if(nums[i]>1):
                nums[i], nums[j]=nums[j],nums[i]
                j-=1
            else:
                i+=1
                