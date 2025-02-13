class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height) - 1
        start = 0
        max = 0
        
        while start <= end:
            distance = end - start
            if height[start] <= height[end]:
                current = height[start] * distance
            elif height[start] > height[end]:
                current = height[end] * distance

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

            if current > max:
                max = current
        return max