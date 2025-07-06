import numpy as np

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        uniq1, counts1 = np.unique_counts(nums1)
        uniq2, counts2 = np.unique_counts(nums2)
        self.s1 = dict(zip(uniq1, counts1))
        self.s2 = dict(zip(uniq2, counts2))
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.s2[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] not in self.s2.keys():
            self.s2[self.nums2[index]] = 1
        else:
            self.s2[self.nums2[index]] += 1


    def count(self, tot: int) -> int:
        cnt = 0
        for key1 in self.s1.keys():
            if key1 <= tot:
                search = tot - key1
                if search in self.s2.keys():
                    cnt += self.s1[key1] * self.s2[search]
        return int(cnt)




# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)