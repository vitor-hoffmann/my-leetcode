class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split(' ')
        current = ['']
        for char in string:
            if char != '':
                current = char
        return len(current)
        