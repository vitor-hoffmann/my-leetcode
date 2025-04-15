class BIT:
    def __init__(self, n):
        self.n = n
        self.fenw = [0] * (n + 1)
        
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.fenw[i] += delta
            i += i & -i
            
    def query(self, i):
        s = 0
        i += 1
        while i:
            s += self.fenw[i]
            i -= i & -i
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        pos_in_nums2 = [0] * n
        for i, v in enumerate(nums2):
            pos_in_nums2[v] = i
            
        arr = [pos_in_nums2[v] for v in nums1]
        
        left = [0] * n
        bit_left = BIT(n)
        for j in range(n):
            left[j] = bit_left.query(arr[j] - 1)
            bit_left.update(arr[j], 1)
        
        right = [0] * n
        bit_right = BIT(n)
        for j in range(n - 1, -1, -1):
            right[j] = bit_right.query(n - 1) - bit_right.query(arr[j])
            bit_right.update(arr[j], 1)
        
        total_triplets = 0
        for j in range(n):
            total_triplets += left[j] * right[j]
        
        return total_triplets
