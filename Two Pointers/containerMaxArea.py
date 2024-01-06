from typing import List
def containerMaxArea(height : List[int]) -> int:
    left = 0
    right = len(height) - 1

    maxSoFar = float("-inf")

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxSoFar = max(maxSoFar, area)

        if height[left] < height[right]:
            left += 1

        else:
            right -= 1

    return maxSoFar

def main():
    height = [1,8,6,2,5,4,8,3,7]
    print(containerMaxArea(height))

if __name__ == "__main__":
    main()
