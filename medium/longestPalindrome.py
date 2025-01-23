class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        palindrome = s[0]
        leng = 1
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                if (j-i+1 > leng and s[i:j+1] == s[i:j+1][::-1]):
                    leng = j-i+1
                    palindrome = s[i:j+1]
        return palindrome