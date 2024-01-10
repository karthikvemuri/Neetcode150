def basicCalculator(s : str) -> int:

    stack = []
    op = '+'
    current = 0

    for c in s + '+':
        if c == ' ':
            continue
        
        elif c.isdigit():
            current = (current * 10) + int(c)

        else:
            if op == '-':
                stack.append(-current)

            elif op =='+':
                stack.append(current)
            
            elif op == '*':
                stack.append(stack.pop() * current)
            
            elif op == '/':
                stack.append(int(stack.pop() / current))
            
            op, current = c, 0

    return sum(stack)

def main():
    s = "3+2*2"
    st = " 3+5 / 2 "

    print(basicCalculator(st))

if __name__== "__main__":
    main()
