class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = str(x)
        b = a[::-1]
        return a == b
        