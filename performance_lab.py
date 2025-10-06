# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    return Counter(numbers).most_common(1)[0][0]

    pass

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) — one pass to count frequencies
- Worst-case: O(n) — same as best, since all elements must be counted
- Average-case: O(n)
- Space complexity: O(n) — storing frequency of each unique element
- Why this approach? Counter is optimized for frequency counting and provides direct access to the most common element
- Could it be optimized? Only marginally; a manual dictionary approach avoids importing but doesn't improve complexity
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    return [x for x in nums if not (x in seen or seen.add(x))]

    pass

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) — all elements are unique
- Worst-case: O(n) — all elements are duplicates except one
- Average-case: O(n)
- Space complexity: O(n) — set stores seen elements
- Why this approach? Efficient and Pythonic; avoids nested loops and preserves order
- Could it be optimized? Using dict.fromkeys() in Python 3.7+ is slightly faster but less flexible for non-hashable types
"""



# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

    pass

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) — early matches found quickly
- Worst-case: O(n) — must scan all elements
- Average-case: O(n)
- Space complexity: O(n) — storing seen elements and pairs
- Why this approach? Hashing allows constant-time lookups and avoids nested loops
- Could it be optimized? Sorting the list and using two pointers gives O(n log n) time but avoids extra space
"""
# -------------------------------
# Optimized Version of Problem #3
# -------------------------------

def find_pairs_optimized(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    pairs = []

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return pairs

"""
Optimization Comparison:
- Original used hashing for O(n) time and O(n) space.
- Optimized version uses sorting and two pointers:
  - Time: O(n log n) due to sort
  - Space: O(1) extra space (excluding output)
- Trade-off: Slightly slower for large inputs, but more memory-efficient.
"""

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    array = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_array = [None] * (capacity * 2)
            for j in range(size):
                new_array[j] = array[j]
            array = new_array
            capacity *= 2
        array[size] = i
        size += 1

    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size == capacity
- Worst-case for a single append: O(n) — during resize and copy
- Amortized time per append overall: O(1)
- Space complexity: O(n) — final array size is proportional to n
- Why does doubling reduce the cost overall? Because the number of resizes grows logarithmically, spreading the cost over many appends
"""



# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

    pass

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) — single pass through list
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) — storing running totals
- Why this approach? Simple and efficient; avoids recomputation
- Could it be optimized? In-place modification reduces space to O(1) if mutation is allowed
"""

# -------------------------------
#  Test Cases for All Problems
# -------------------------------

def test_most_frequent():
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([1, 1, 2, 2]) in [1, 2]  # tie
    assert most_frequent([5]) == 5
    assert most_frequent([]) == None

def test_remove_duplicates():
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_find_pairs():
    assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
    assert set(find_pairs([1, 2, 3], 6)) == set()
    assert set(find_pairs([], 5)) == set()
    assert set(find_pairs([0, 5, -5, 10], 5)) == {(0, 5), (-5, 10)}

def test_add_n_items():
    add_n_items(6)  # should print resizing events

def test_running_total():
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total([5]) == [5]
    assert running_total([0, 0, 0]) == [0, 0, 0]

# Run all tests
test_most_frequent()
test_remove_duplicates()
test_find_pairs()
test_add_n_items()
test_running_total()

print("✅ All tests passed.")

