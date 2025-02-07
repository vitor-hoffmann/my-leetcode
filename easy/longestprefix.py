class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    # Pega a menor string, pois o prefixo comum não pode ser maior que ela
    prefix = min(strs, key=len)

    for i, char in enumerate(prefix):
        for string in strs:
            if string[i] != char:
                return prefix[:i]  # Retorna o prefixo até o índice anterior

    return prefix
        