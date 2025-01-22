class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1len = len(nums1)
        nums2len = len(nums2)
        
        if nums1len > nums2len:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = nums1len + nums2len
        left = (nums1len + nums2len + 1) // 2 
        low = 0
        high = nums1len
        
        while low <= high:
            mid1 = (low + high) // 2 
            mid2 = left - mid1 
            
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            if mid1 < nums1len:
                r1 = nums1[mid1]
            if mid2 < nums2len:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0 