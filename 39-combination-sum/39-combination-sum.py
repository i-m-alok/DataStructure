class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.findCombinations(candidates, target, 0, result, [])
        return result
    
    def findCombinations(self, nums, target, index, result, buffer):
        # print(buffer, target)
        if(target==0):
            result.append(list.copy(buffer))
            return
        if(target<0 or index>=len(nums)):
            return 
        # pick current element
        buffer.append(nums[index])
        self.findCombinations(nums, target-nums[index], index, result, buffer)
        if(len(buffer)):
            del buffer[-1]
        self.findCombinations(nums, target, index+1, result, buffer)
        return
    