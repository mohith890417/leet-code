class Solution:

  def reverse(self, x: int) -> int:
    # Define the 32-bit signed integer limits
    MIN_INT = -2**31
    MAX_INT = 2**31 - 1

    # Handle the sign of the number
    sign = -1 if x < 0 else 1
    x = abs(x)

    reversed_num = 0
    while x != 0:
      digit = x % 10
      x //= 10

      # Check for 32-bit overflow before appending the digit
      if reversed_num > (MAX_INT - digit) // 10:
        return 0

      reversed_num = reversed_num * 10 + digit

    return sign * reversed_num