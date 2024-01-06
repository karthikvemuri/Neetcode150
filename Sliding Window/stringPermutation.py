def stringPermutation(s1 :str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    s1Map = {}
    s2Map = {}
    
    for i in range(len(s1)):
        s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
        s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)

    
    l = 0
    for r in range(len(s1), len(s2)):
        if s1Map == s2Map:
            return True

        s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)
        s2Map[s2[l]] -= 1

        if s2Map[s2[l]] == 0:
            s2Map.pop(s2[l])

        l += 1

    return s1Map == s2Map


def main():
    a = "ab"
    b = "eidpaooo"
    print(stringPermutation(a, b))


if __name__ == "__main__":
    main()


