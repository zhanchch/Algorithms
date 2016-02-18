class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_ending = nums[0]
        min_ending = nums[0]
        max_product = nums[0]

        i = 1
        while i < n:
            max_temp = max_ending
            min_temp = min_ending

            max_ending = max(max(max_temp * nums[i], min_temp * nums[i]), nums[i])
            min_ending = min(min(max_temp * nums[i], min_temp * nums[i]), nums[i])

            max_product = max(max_ending, max_product)

            i += 1

        return max_product

