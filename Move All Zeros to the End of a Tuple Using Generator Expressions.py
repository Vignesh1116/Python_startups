# Move All Zeros to the End of a Tuple Using Generator Expressions

number = (1,2,1,2,0,0,1,2,1,2,1,2,1)

b = (n for n in number if n != 0)
zero = (n for n in number if n == 0)
print(list(b)+list(zero))