class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        expected_sum = (total_numbers * (total_numbers + 1)) // 2
        
        seen = set()
        actual_sum = 0
        repeated = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)
                actual_sum += num

        missing = expected_sum - (actual_sum - repeated)
        return [repeated, missing]
