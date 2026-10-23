class Solution:

  def compress(self, chars: List[str]) -> int:
    write = 0
    i = 0
    n = len(chars)

    while i < n:
      j = i
      # Find the end of the current consecutive group of characters
      while j < n and chars[j] == chars[i]:
        j += 1

      # Write the character
      chars[write] = chars[i]
      write += 1

      count = j - i
      # If the count is greater than 1, append its digits
      if count > 1:
        for digit in str(count):
          chars[write] = digit
          write += 1

      # Move to the next new character group
      i = j

    return write