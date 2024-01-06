from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    result = defaultdict(list)

    for s in strs:

        count = [0] * 26

        for c in s:

            count[ord(c) - ord("a")] += 1
        
        result[tuple(count)].append(s)

    return result.values()

def main():

    strs = ["eat","tea","tan","ate","nat","bat"]

    print(groupAnagrams(strs))

if __name__ == "__main__":
    main()
