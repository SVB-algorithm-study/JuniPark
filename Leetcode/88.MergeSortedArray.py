class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

        # nums1 += nums2
        # # nums1 = nums1.sort()
        # # print(nums1)
        # cnt = nums1.count(0)
        # nums1 = nums1.sort()
        # nums1 = nums1[cnt:]


        # cnt = 0
        # for i in range(len(nums1)):
        #     if nums1[i] == 0 :
        #         cnt +=1
        # print(cnt)
        # nums1 = nums1[cnt:]
