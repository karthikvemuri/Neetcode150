def charReplacement(s : str, k : int) -> int:

    count = {}
    result = 0
    start = 0
    
    for end in range(len(s)):
        count[s[end]] = 1 + count.get(s[end], 0)

        while (end - start + 1) - max(count.values()) > k:
            count[s[start]] -= 1
            start += 1

        result = max(result, end - start + 1)
    return result

def main():
    s = "ABAB"
    k = 2
    print(charReplacement(s, k))

if __name__ == "__main__":
    main()
