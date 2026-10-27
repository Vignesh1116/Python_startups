# Find the First Non-Repeating Character in a String

s = "aabbcdde"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break