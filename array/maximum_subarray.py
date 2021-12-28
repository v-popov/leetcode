# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] # can't set to 0, as nums can contain negative values
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sum = max(max_sum, cur_sum)

        return max_sum