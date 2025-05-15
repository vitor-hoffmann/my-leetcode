class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []
        
        res = [words[0]]
        last_group = groups[0]
        
        for word, grp in zip(words[1:], groups[1:]):
            if grp != last_group:
                res.append(word)
                last_group = grp
        
        return res
