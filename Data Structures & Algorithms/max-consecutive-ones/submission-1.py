class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # max_consec_ones = 0
        # tmp_max_consec_ones = 0
        # prev_seen = 1
        # for num in nums:
        #     if prev_seen == num:
        #         tmp_max_consec_ones += 1
        #         prev_seen = num
        #     else:
        #         max_consec_ones = max(max_consec_ones, tmp_max_consec_ones)
        #         tmp_max_consec_ones = 0
        # return max(max_consec_ones, tmp_max_consec_ones)

        result = count = 0
        for num in nums:
            count += 1 if num else -count
            result = max(result, count)
        
        return result
                

        