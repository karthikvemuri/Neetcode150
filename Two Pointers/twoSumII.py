from typing import List
def twoSumII(nums : List[int], target : int) -> List[int]:

    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left + 1, right + 1]
        
        elif sum < target:
            left += 1
        
        else:
            right -= 1

def main():
    nums = [2,3,4]
    target = 6
    print(twoSumII(nums, target))

if __name__ == "__main__":
    main()

