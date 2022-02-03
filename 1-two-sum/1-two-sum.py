class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        subMap = {}
        for i in range(len(nums)):
            ele = nums[i]
            if(subMap.get(ele)!=None):
                return (i, subMap[ele])
            subMap[target-ele]=i