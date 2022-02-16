class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        # we know a^a=0
        # ones will contain single occured no.
        # two will contain no.s with occurance two
        # one=0, two=0 means initial state or no. with occurance 3
        # one=0, two=i means i is repeated
        for i in nums:
            ones = (ones^i)&(~twos)
            twos = (twos^i)&(~ones)
        return ones