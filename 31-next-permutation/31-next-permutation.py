class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find smallest index
        # minVal = nums[-1]
        # minIndex = len(nums)-1
        i=len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        #find next greater
        minIndex=i
        # print(minVal,minIndex,i)
        j=len(nums)-1
        while(j>=0 and minIndex>=0):
            if(nums[j]>nums[minIndex]):
                nums[j], nums[minIndex] = nums[minIndex], nums[j]
                break
            j-=1
        # reverse the array from next index of minIndex to end 
        i = minIndex+1
        j = len(nums)-1
        while(i<j):
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        return