from typing import List
def productExceptSelf(nums : List[int]) -> List[int] : 

    result = [0] * len(nums)

    pre = 1

    for i in range(len(nums)):
        result[i] = pre
        pre = pre * nums[i]
    
    post = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post = post * nums[i]
    
    return result

def main():
    nums = [-1,1,0,-3,3]

    print(productExceptSelf(nums))

if __name__ == "__main__":
    main()

