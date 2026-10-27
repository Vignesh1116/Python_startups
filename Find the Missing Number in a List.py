# Find the Missing Number in a List

nums = [1, 2, 3, 5]
n = 5

missing = n * (n + 1) // 2 - sum(nums)
print(missing)