class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end= 0
        while(start<len(nums)):
            if(nums[start]<1):
                self.swap(nums, start,end)
                start+=1
                end+=1
            else:
                start+=1
        start=len(nums)-1
        end=len(nums)-1
        while(start>=0):
            if(nums[start]>1):
                self.swap(nums, start,end)
                start-=1
                end-=1
            else:
                start-=1
        print(nums)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i]=nums[j]
        nums[j]=temp