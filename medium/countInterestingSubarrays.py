class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        pref = 0
        ans = 0
        
        for x in nums:
            pref = (pref + (1 if x % modulo == k else 0)) % modulo
            
            target = (pref - k) % modulo
            ans += count[target]
            
            count[pref] += 1
        
        return ans
