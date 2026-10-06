n = int(input("Enter the number of elements:"))

arr = []

for i in range(n):
    num = int(input("Enter the element:"))
    arr.append(num)

sum = 0

for i in range(n):
    sum = sum + arr[i]

print("Sum of all elements:", sum)