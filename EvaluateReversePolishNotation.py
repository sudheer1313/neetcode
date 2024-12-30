

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i == '+':
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(p2) + int(p1)
                stack.append(res)
            elif i == '-':
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(p2) - int(p1)
                stack.append(res)
            elif i == '*':
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(p2) * int(p1)
                stack.append(res)
            elif i == '/':
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(p2) / int(p1)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[0])
