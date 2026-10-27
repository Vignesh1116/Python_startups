# Print Duplicate Characters in a String

s = "programming"

for ch in s:
    if s.count(ch) > 1:
        print(ch, end=" ")
        s = s.replace(ch, "", 1)