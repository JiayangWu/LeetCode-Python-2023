"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id2imp = dict()
        sup2sub = dict()

        for i, ee in enumerate(employees):
            idd, imp, subs = ee.id, ee.importance, ee.subordinates
            id2imp[idd] = imp
            sup2sub[idd] = subs
        
        def dfs(node):
            if not node:
                return 0
            res = id2imp[node] 
            for sub in sup2sub[node]:
                res += dfs(sub)
            return res

        return dfs(id)