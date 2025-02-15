class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs.values():  # Se for parêntese de abertura
                stack.append(char)
            elif char in pairs.keys():  # Se for parêntese de fechamento
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                return False

        return not stack  # Retorna True se a pilha estiver vazia
