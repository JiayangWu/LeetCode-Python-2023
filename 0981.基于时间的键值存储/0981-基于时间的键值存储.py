class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.key2valTs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key2valTs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key2valTs and timestamp >= self.key2valTs[key][0][0]:
            # binary search self.key2valTs[key]
            l = self.key2valTs[key]
            left, right = 0, len(self.key2valTs[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if l[mid][0] == timestamp:
                    return l[mid][1]
                elif l[mid][0] < timestamp:
                    left = mid + 1
                elif l[mid][0] > timestamp:
                    right = mid - 1
            return l[right][1]
        else:   
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)