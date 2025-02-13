from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Ordena para facilitar a busca
        res = []
        size = len(nums)

        for i in range(size - 2):  # O último possível i é size-3, pois precisamos de 3 elementos
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Evita repetir números iguais como primeiro elemento
            
            left, right = i + 1, size - 1  # Ponteiros

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Evita duplicatas
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move os ponteiros para continuar buscando outras combinações
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Precisamos de um número maior
                else:
                    right -= 1  # Precisamos de um número menor

        return res
