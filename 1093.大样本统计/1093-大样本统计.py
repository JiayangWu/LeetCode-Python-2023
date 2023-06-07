class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum, median, maximum, mean, mode = None, None, None, None, None
        s, total_count, cur_count = 0, 0, 0
        for i, x in enumerate(count):
            if x and minimum is None:
                minimum = i
            s += x * i
            total_count += x

        mean = s * 1.0 / total_count
        mode = count.index(max(count))

        for i in range(len(count)):
            if count[i]:
                cur_count += count[i]
                if median is None:
                    if total_count % 2 == 1:
                        if cur_count >= total_count // 2 + 1:
                            median = i
                    else:
                        if cur_count > total_count // 2:
                            median = i
                        if cur_count == total_count // 2:
                            for j in range(i + 1, len(count)):
                                if count[j]:
                                    break
                            median = (i + j) / 2.0
                else:
                    break

        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                maximum = i
                break

        return [minimum, maximum, mean, median, mode]
        


        