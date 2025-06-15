class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["*", "/", "+", "-"])
        stk = []

        for token in tokens:
            if token not in ops:
                stk.append(int(token))
            else:
                num2 = stk.pop()
                num1 = stk.pop()

                if token == "*":
                    stk.append(num1*num2)
                elif token == "/":
                    stk.append(int(num1/num2))
                elif token == "+":
                    stk.append(num1+num2)
                else:
                    stk.append(num1-num2)
        
        return stk[0]