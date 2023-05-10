class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # for문 안에 sum 쓰는거 주의하기
            # 시간이 엄청 오래 걸림
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1