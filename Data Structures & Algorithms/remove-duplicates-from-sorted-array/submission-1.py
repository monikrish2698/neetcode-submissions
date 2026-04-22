class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # l = r = 0
        # while (r < n):
        #     nums[l] = nums[r]
        #     while (r < n) and nums[r] == nums[l]:
        #         r += 1
        #     l += 1
        # return l
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l