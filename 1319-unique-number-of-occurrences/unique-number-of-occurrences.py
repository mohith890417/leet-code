class Solution:

  def uniqueOccurrences(self, arr: list[int]) -> bool:
    # Step 1: Count the occurrences of each number using a hash map
    count = {}
    for num in arr:
      count[num] = count.get(num, 0) + 1

    # Step 2: Compare the number of unique values with the number of unique frequencies
    # If the length of frequencies (set of values) equals the length of keys (unique elements),
    # it means all occurrence counts are unique.
    return len(set(count.values())) == len(count)