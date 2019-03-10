class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}  # Int -> Int
        for idx, num in enumerate(nums):
            numdict[num] = idx
        for idx_target, num in enumerate(nums):
            complement = target - num
            if complement in numdict and numdict[complement] != idx_target:
                return list((idx_target, numdict[complement]))

