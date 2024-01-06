def validParentheses(s : str) -> bool:

    stack = []
    pMap = {")" : "(", "]" : "[", "}" : "{"}

    for c in s:
        if c in pMap:
            if stack and stack[-1] == pMap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


def main():
    s = "()[]{}"
    print(validParentheses(s))

if __name__ == "__main__":
    main()