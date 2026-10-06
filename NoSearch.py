n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter number to search: "))

found = 0

for i in range(n):
    if arr[i] == search:
        print("Number is present")
        print("Position:", i + 1)
        found = 1
        break

if found == 0:
    print("Number is not present in the array")