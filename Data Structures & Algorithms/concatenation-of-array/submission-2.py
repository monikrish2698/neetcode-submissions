class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_arr = [0] * 2*n
        for i in range(0, n):
            new_arr[i] = new_arr[i+n] = nums[i]
        return new_arr