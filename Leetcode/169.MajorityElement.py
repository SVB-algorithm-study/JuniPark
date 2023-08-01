class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # major_num = 0
        # major_cnt = 0
        # checked_num = []

        # for i in nums:
        #     if i not in checked_num:
        #         if nums.count(i) > major_cnt :
        #             major_num = i
        #             major_cnt = nums.count(i)
        #             checked_num.append(i)

        # return major_num

        n = len(nums)
        nums.sort()
        if n%2 == 1 :
            return nums[int((n-1)/2)]
        else :
            return nums[int(n/2)]