class Solution:

  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)

    for i in range(length):
      # Check if the current plot is empty
      if flowerbed[i] == 0:
        # Check if the left plot is empty (or it's the start of the array)
        empty_left = (i == 0) or (flowerbed[i - 1] == 0)
        # Check if the right plot is empty (or it's the end of the array)
        empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

        # If both sides are empty, we can plant a flower here
        if empty_left and empty_right:
          flowerbed[i] = 1  # Plant the flower
          count += 1
          if count >= n:
            return True

    return count >= n
        