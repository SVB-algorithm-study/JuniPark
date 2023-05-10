class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_num = sum(nums) 
        prev_num = 0
        for i in range(len(nums)):
            last_num = sum_num - prev_num - nums[i]
            if prev_num == last_num:
                return i
            prev_num += nums[i]
        return -1