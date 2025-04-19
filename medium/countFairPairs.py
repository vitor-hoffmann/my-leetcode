class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i, x in enumerate(nums):
            lo = lower - x
            hi = upper - x
            
            L = bisect_left(nums, lo, i+1, n)
            R = bisect_right(nums, hi, i+1, n)
            
            count += (R - L)
        
        return count
