class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        nums = [[1], [1, 1]]
        for i in range(2, numRows):
            arr = [1]
            for j in range(1, i):
                arr.append(nums[i - 1][j - 1] + nums[i - 1][j])
            arr.append(1)
            nums.append(arr)

        return nums


Solution.generate(Solution, 6)