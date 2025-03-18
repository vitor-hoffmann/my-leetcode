class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bit_mask = 0
        max_length = 0

        for right in range(len(nums)):
            while (bit_mask & nums[right]) != 0:
                bit_mask ^= nums[left]  
                left += 1 

            bit_mask |= nums[right]

            max_length = max(max_length, right - left + 1)

        return max_length