class Solution:

  def minOperations(self, s: str) -> int:
    # If already sorted
    if s == "".join(sorted(s)):
      return 0

    n = len(s)
    if n <= 1:
      return 0

    mn = min(s)
    mx = max(s)

    # Check if impossible (like length 2 in descending order)
    if n == 2 and s[0] > s[1]:
      return -1

    # If mn appears at the beginning (not whole string) or mx appears at the end (not whole string)
    if (s[0] == mn and s != mn * n) or (s[-1] == mx and s != mx * n):
      return 1

    # Check if mn exists in any proper prefix or mx exists in any proper suffix
    has_mn_prefix = mn in s[:-1]
    has_mx_suffix = mx in s[1:]

    if not has_mn_prefix and not has_mx_suffix:
      return 3
    else:
      return 2