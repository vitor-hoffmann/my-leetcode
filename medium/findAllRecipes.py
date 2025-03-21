class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        
        ingredient_to_recipes = {recipe: [] for recipe in recipes}
        in_degree = {recipe: 0 for recipe in recipes}  
        
        for recipe, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                if ing not in available:  
                    in_degree[recipe] += 1
                    if ing in ingredient_to_recipes: 
                        ingredient_to_recipes[ing].append(recipe)

        queue = deque()
        for recipe in recipes:
            if in_degree[recipe] == 0:
                queue.append(recipe)
        
        result = []
        while queue:
            recipe = queue.popleft()
            result.append(recipe) 
            available.add(recipe)  

            for dependent_recipe in ingredient_to_recipes[recipe]:
                in_degree[dependent_recipe] -= 1
                if in_degree[dependent_recipe] == 0: 
                    queue.append(dependent_recipe)

        return result
