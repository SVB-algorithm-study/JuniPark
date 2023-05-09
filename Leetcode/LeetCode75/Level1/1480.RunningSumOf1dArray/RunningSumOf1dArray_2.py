class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_arr = []
        for i in range(1,len(nums)+1) :
            result_arr.append(sum(nums[:i]))
        return result_arr