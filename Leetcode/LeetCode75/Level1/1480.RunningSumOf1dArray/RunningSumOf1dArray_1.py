class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_arr = []
        sum_num = 0
        for i in nums :
            sum_num += i
            result_arr.append(sum_num)
        return result_arr