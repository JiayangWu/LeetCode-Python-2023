class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combine = [(name, heights[index]) for index, name in enumerate(names)]
        combine.sort(key = lambda x: -x[1])
        return [pair[0] for pair in combine]