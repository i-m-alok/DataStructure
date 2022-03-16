class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        
        ptr=len(nums)-1
        while(low<high and low<=ptr):
            # print(nums, low, ptr, high)
            if(nums[ptr]<1):
                nums[ptr], nums[low] = nums[low], nums[ptr]
            if(nums[ptr]>=1):
                nums[ptr], nums[high] = nums[high], nums[ptr]
                ptr-=1
            if(nums[high]>1):
                high-=1
            if(nums[low]<1):
                low+=1
            # ptr-=1