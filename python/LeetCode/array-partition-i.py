class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0
        count = (len(nums) // 2) + if len(nums) > 2 else 1 
        array_pairs = [(nums[i], nums[i + 1]) for x in range(0, len(nums) // 2, 2)]
        for pair in array_pairs():
            result += min(pair[0], pair[1])
        return result

# this solution is inefficient because you don't need to store the pairs...