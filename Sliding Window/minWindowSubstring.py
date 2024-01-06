def minWindow(s : str, t : str) -> str :

    if t == "":
        return ""

    tMap = {}
    sMap = {}

    for c in t:
        tMap[c] = 1 + tMap.get(c, 0)

    have = 0
    need = len(tMap)
    res = [-1, -1]
    minLen = float("inf")

    l = 0

    for r in range(len(s)):
        c = s[r]
        sMap[c] = 1 + sMap.get(c, 0)

        if c in tMap and sMap[c] == tMap[c]:
            have += 1

        while have == need:
            if (r - l + 1) < minLen:
                minLen = r - l + 1
                res = [l , r]
            sMap[s[l]] -= 1

            if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1] if minLen != float("inf") else ""

def main():
    s = "ADOBECODEBANC" 
    t = "ABC"
    print(minWindow(s, t))

if __name__ =="__main__":
    main()
            







    