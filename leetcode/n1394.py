import numpy as np

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        uniq, counts = np.unique_counts(arr)
        arr = [(-1, -1)] + list(zip(uniq, counts))

        return max(int(i) for i, j in arr if i == j)
