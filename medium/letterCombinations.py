class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return [] 

        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        queue = [""] 

        for digit in digits:
            possible_letters = letters[digit] 
            new_combinations = []  

            for combination in queue:
                for letter in possible_letters:
                    new_combinations.append(combination + letter)
            queue = new_combinations

        return queue