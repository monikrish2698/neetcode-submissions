class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin = 0
        list_cnt = len(nums)
        for j in range(0, list_cnt):
            if nums[j] != val:
                nums[begin] = nums[j]
                begin += 1
        return begin
        