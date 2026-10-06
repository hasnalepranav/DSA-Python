n = int(input("Enter the number of elements:"))

arr = []

for i in range(n):
    num = int(input("Enter element:"))
    arr.append(num)

arr.sort()

print("Smallest:", arr[0])
print("Second Smallest:", arr[1])
print("Second Largest:", arr[n-2])
print("Largest:", arr[n-1])

# arr = [10,2,45,6,8,23,42,38,56]
# max = min = arr[0]
# smin = smax = arr[0]
# for num in arr:
#     if num>max:
#         smax=max
#         max=num
#     elif (num>smax and num!=max):
#         smax=num
#     if num<min:
#         smin=min
#         min=num
#     elif (num<smin and num!=min):
#         smin=num

# print("Smallest:", min)
# print("Second smallest:", smin)
# print("Largest:", max)
# print("Second Largest:", smax)

