class Solution:

  def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    stack = []
    for ast in asteroids:
      # Collision happens only if stack top is positive and current asteroid is negative
      while stack and stack[-1] > 0 and ast < 0:
        if abs(stack[-1]) < abs(ast):
          stack.pop()  # The top asteroid explodes, continue checking
          continue
        elif abs(stack[-1]) == abs(ast):
          stack.pop()  # Both explode
        break  # Current asteroid explodes or both exploded
      else:
        stack.append(ast)  # No collision or current asteroid survived
    return stack