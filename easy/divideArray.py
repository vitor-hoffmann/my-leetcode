class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return all(freq % 2 == 0 for freq in count.values())