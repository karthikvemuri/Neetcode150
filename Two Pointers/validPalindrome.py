def isAlphaNumeric(ch) -> bool:
    return (
        ord("A") <= ord(ch) <= ord("Z") or
        ord("a") <= ord(ch) <= ord("z") or
        ord("1") <= ord(ch) <= ord("9")
    )

def validPalindrome(s : str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not isAlphaNumeric(s[left]):
            left += 1
        
        while left < right and not isAlphaNumeric(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

def main():
    s = "race a car"
    t = "A man, a plan, a canal: Panama"

    print(validPalindrome(s))
    print(validPalindrome(t))

if __name__ == "__main__":
    main()


