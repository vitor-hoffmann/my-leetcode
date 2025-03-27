class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = Counter(words)
        total_len = word_len * len(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            window_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                window_count[word] += 1
                
                while window_count[word] > word_count[word]:
                    window_count[s[left:left + word_len]] -= 1
                    left += word_len
                
                if right - left == total_len:
                    result.append(left)
        
        return result
