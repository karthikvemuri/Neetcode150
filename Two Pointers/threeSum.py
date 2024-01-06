from typing import List
def threeSum(nums : List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            threeSum = nums[i] + nums[left] + nums[right]

            if threeSum > 0:
                right -= 1

            elif threeSum < 0:
                left += 1

            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result

def main():
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))

if __name__ == "__main__":
    main() 