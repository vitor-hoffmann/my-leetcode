class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            left_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left_index = mid
                    right = mid - 1  
            return left_index

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            right_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    right_index = mid
                    left = mid + 1  
            return right_index

        return [findLeft(nums, target), findRight(nums, target)]
