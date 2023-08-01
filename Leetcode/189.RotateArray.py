class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Time Limit
        # for _ in range(k):
        #     nums[:]= [nums[-1]] + nums[:-1]

        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]