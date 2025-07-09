

class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        self.arr = []
        def iscurrect(s: str):
            while s.find("()") + 1:
                s = s.replace("()", "", -1)
            return not len(s)



        def f(n, open=0, close=0, s=""):
            if (open == close) and ((open + close) == n) and iscurrect(s):
                self.arr.append(s)
            elif (open + close) > n:
                return

            return f(n, open + 1, close, s + "("), f(n, open, close + 1, s + ")")

        f(n * 2)
        #print(self.arr)
        return self.arr


