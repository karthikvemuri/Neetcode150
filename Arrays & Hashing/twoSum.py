from typing import List

def twoSum(nums : List[int], target: int) -> List[int]:

    hMap = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in hMap:
            return [hMap.get(diff), i]

        hMap[nums[i]] = i

def main():
    nums = [2,7,11,15]
    target = 26

    print(twoSum(nums, target))

if __name__=="__main__":
    main()

