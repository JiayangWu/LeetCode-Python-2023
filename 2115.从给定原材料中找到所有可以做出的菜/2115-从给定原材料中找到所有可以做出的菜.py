class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque
        indegree = defaultdict(int)
        src2des = defaultdict(list)

        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                src2des[ing].append(recipes[i])
            indegree[recipes[i]] += len(ingredient)

        queue = deque()
        for s in supplies:
            queue.append(s)

        supplies = set(supplies)

        res = []
        while queue:
            cur = queue.popleft()
            if cur not in supplies:
                res.append(cur)

            for recipe in src2des[cur]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
        
        return res
