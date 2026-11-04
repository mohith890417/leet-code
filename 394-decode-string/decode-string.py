class Solution:

  def decodeString(self, s: str) -> str:
    stack = []
    current_string = ""
    current_k = 0

    for char in s:
      if char.isdigit():
        current_k = current_k * 10 + int(char)
      elif char == "[":
        # Push the current state to stack and reset
        stack.append((current_string, current_k))
        current_string = ""
        current_k = 0
      elif char == "]":
        # Pop the previous string and the repeat count
        prev_string, k = stack.pop()
        current_string = prev_string + current_string * k
      else:
        current_string += char

    return current_string