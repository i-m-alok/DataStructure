class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxCount=0
        maxItem=None
        count=0
        lastItem=None
        print(nums)
        for i in nums:
            print(i, lastItem, count)
            if(lastItem!=i):
                if(count>maxCount):
                    maxCount=count
                    maxItem=lastItem
                count=1
                lastItem=i
            else:
                count+=1
        if(count>maxCount):
            return lastItem
        return maxItem