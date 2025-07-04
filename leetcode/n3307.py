class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        next_symbol = lambda c: chr((ord(c) == ord("z")) * ord("a") + (ord(c) != ord("z")) * (ord(c) + 1))
        ln = 2 ** len(operations)
        cnt_reverse = 0

        for i in range(len(operations) - 1, -1, -1):
            if (ln // 2) < k:
                cnt_reverse += (operations[i] == 1)
            ln //= 2
            if (k > ln):
                if not k % ln:
                    k = ln
                else:
                    k = (k % ln)

        ans = "a"
        for i in range(cnt_reverse):
            ans = next_symbol(ans)


        return ans