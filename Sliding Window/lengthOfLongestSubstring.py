def lengthOfLongestSubstring(s : str) -> int:

    start = 0

    maxLength = 0
    charSet = set()

    for end in range(len(s)):
        while s[end] in charSet:
            charSet.remove(s[start])
            start += 1

        charSet.add(s[end])
        maxLength = max(maxLength, end - start + 1)

    return maxLength

def main():
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))

if __name__=="__main__":
    main()