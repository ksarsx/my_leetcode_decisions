import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = [] # массив, хранящий соедининие nums1 и nums2 в один массив, сохраняя порядок
        ij = [0, 0] # индексы, элементов массивов, по которым проходимся

        f1 = lambda ij: ij[0] < len(nums1)
        f2 = lambda ij: ij[1] < len(nums2)

        # процесс формирования arr
        while f1(ij) or f2(ij):
            if f1(ij) and f2(ij):
                arr.append(min(nums1[ij[0]], nums2[ij[1]]))
                ij[np.argmin([nums1[ij[0]], nums2[ij[1]]])] += 1
            elif f1(ij):
                arr.append(nums1[ij[0]])
                ij[0] += 1
            else:
                arr.append(nums2[ij[1]])
                ij[1] += 1


        sz = len(arr)

        if not sz % 2:
            return (arr[sz // 2 - 1] + arr[sz // 2]) / 2
        return arr[sz // 2]


print(Solution.findMedianSortedArrays(Solution, [1,2], [3,4]))