# Count Alphanumeric Characters in a String

s = "hello world!@123"
freq = {}

for ch in s:
    if ch.isalnum():
        freq[ch] = freq.get(ch, 0) + 1

print(freq)