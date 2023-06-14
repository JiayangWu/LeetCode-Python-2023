class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        target = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        for i in range(1, len(skill) // 2):
            if skill[i] + skill[-i-1] != target:
                return -1
            else:
                res += skill[i] * skill[-i-1]
        return res