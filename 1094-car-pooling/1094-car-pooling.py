class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currentCapacityMap = [0]*1001
        for i in trips:
            start = i[1]
            end = i[2]
            currentCapacityMap[start]+=i[0]
            currentCapacityMap[end]-=i[0]
        currentCapacity = currentCapacityMap[0]
        for value in currentCapacityMap:
            currentCapacity+=value
            print(value, currentCapacity)
            if(currentCapacity>capacity):
                return False
        return True