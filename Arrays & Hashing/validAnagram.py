def validAnagram(s : str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sMap = {}
    tMap = {}

    for i in range(len(s)):
        sMap[s[i]] = 1 + sMap.get(s[i], 0)
        tMap[t[i]] = 1 + tMap.get(t[i], 0)

    return sMap == tMap

def main():
    s = "anagram"
    t = "nagaram"

    print(validAnagram(s, t))

if __name__ == "__main__":
    main()

