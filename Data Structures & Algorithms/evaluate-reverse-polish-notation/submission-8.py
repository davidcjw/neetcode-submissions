class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if self.isOperand(tokens[i]):
                if len(stack) < 2:
                    break
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(int(num1 / num2))
                elif tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
            else:
                # encountered an integer
                stack.append(int(tokens[i]))
        
        return stack.pop()

    def isOperand(self, operand) -> bool:
        return operand in ["*", "/", "+", "-"]
