n = int(input("Enter the no of elements:"))

arr = []

for i in range(n):
    num = int(input("Enter elements:"))
    arr.append(num)

even = 0
odd = 0

for i in range(n):
    if arr[i] %2 == 0:
        even += 1
    else:
        odd += 1

print("Even Count:", even)
print("Odd Count:", odd)
