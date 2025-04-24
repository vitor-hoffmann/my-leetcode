class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        
        left = 0
        current_count = defaultdict(int)
        result = 0
        
        for right in range(len(nums)):
            current_count[nums[right]] += 1
            
            while len(current_count) == distinct_count:
                result += len(nums) - right  
                current_count[nums[left]] -= 1
                if current_count[nums[left]] == 0:
                    del current_count[nums[left]]
                left += 1
        
        return result
