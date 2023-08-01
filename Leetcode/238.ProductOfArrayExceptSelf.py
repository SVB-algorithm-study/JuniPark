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

        # 각 원소의 왼쪽 부분 곱 계산
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # 각 원소의 오른쪽 부분 곱 계산
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
            
        # 정답 계산
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer