from typing import List
def longestConsecutiveSequence(nums : List[int]) -> int:
    longest = 0

    numSet = set(nums)

    for num in nums:
        if num - 1 not in numSet:
            length = 0

            while (num + length) in numSet:
                length += 1

            longest = max(length, longest)

    return longest  


def main():
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutiveSequence(nums))

if __name__ == "__main__":
    main()
