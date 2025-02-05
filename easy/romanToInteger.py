class Solution:
    def romanToInt(self, s: str) -> int:
        value_symbols = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        left = 0
        num = 0
        while left < len(s):
            if left + 1 < len(s) and s[left:left + 2] in value_symbols:
                num += value_symbols[s[left:left + 2]]
                left += 2 
            else:
                num += value_symbols[s[left]]
                left += 1 
            
        return num