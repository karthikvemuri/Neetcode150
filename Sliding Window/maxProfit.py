from typing import List
def maxProfit(prices : List[int]) -> int:
    left = 0
    right = 1

    profit = 0
    maxGain = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxGain = max(profit, maxGain)

        else:
            left = right
        right += 1

    return maxGain

def main():
    prices = [7,6,4,3,1]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()
