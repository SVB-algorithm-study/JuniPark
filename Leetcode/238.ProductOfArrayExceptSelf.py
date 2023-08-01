class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # answer = []
        # for i in nums:
        #     ans = 1
        #     for j in nums :
        #         if i != j :
        #             ans *= j
        #     answer.append(ans)
        # return answer

        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        # Calculate the product of the left part of each element
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate the right partial product of each element
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
            
        # Calculate the answer
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer