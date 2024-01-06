from typing import List
def containsDuplicates(nums : List[int]) -> bool:
    hSet = set()

    for num in nums:
        if num in hSet:
            return True
        hSet.add(num)

    return False

def main():
    nums = [1, 2, 3, 4, 5, 8, 5]
    print(containsDuplicates(nums))

if __name__ == "__main__":
    main()








