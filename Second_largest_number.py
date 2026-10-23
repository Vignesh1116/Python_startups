# Second Largest Number

a = [10, 20, 5, 8, 15]

largest = a[0]
second = a[0]

for n in a:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)