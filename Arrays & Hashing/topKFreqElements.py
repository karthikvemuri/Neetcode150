from typing import List
def topKFreqElements(nums : List[int] , k : int) -> List[int]:

    countMap = {}

    frequency = [[] for i in range(len(nums) + 1)]

    for num in nums:
        countMap[num] = 1 + countMap.get(num, 0)

    for n, c in countMap.items():
        frequency[c].append(n)

    result = []

    for i in range(len(frequency) - 1, 0, -1):

        for j in frequency[i]:
            result.append(j)

        if len(result) == k:
            return result


def main():
    nums = [1,2,3,4,5,2,1] 
    k = 2

    print(topKFreqElements(nums, k))

if __name__ == "__main__":
    main()



