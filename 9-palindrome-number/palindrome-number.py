class Solution:

  def isPalindrome(self, x: int) -> bool:
    # Negative numbers and numbers that end with 0 (except 0 itself) cannot be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    reversed_half = 0
    while x > reversed_half:
      reversed_half = reversed_half * 10 + x % 10
      x //= 10

    # If the length is odd, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10