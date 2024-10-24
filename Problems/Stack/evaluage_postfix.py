def evalRPN(tokens):
        def checktype(i):
            try:
                int(i)
                return True
            except ValueError:
                return False
        stack = []
        for i in tokens:
            if checktype(i):
                stack.append(i)
            else:
                if len(stack) > 1:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if i == '+':
                        c = a + b
                    elif i == '-':
                        c = a - b
                    elif i == '*':
                        c = a * b
                    elif i == '/':
                        c = int(b/a)
                    stack.append(c)
        return stack[0]

if __name__ == '__main__':
    line = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(line))