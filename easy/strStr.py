class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letters = re.split('(' + re.escape(needle) + ')', haystack)
        idx = 0
        for char in letters:
            if char == needle:
                return idx
            idx += len(char)
        return -1
        