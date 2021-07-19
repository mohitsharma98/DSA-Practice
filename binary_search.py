a = [3,5,7,8,12,17,22]
target = 9

def binary_search(a, target):
    left=0
    right=len(a)-1
    mid = (left+right)//2

    for i in range(0, len(a)//2):
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid 
            mid  = (left+right)//2
        elif a[mid] > target:
            right = mid
            mid = (left+right)//2
    return -1

print(binary_search(a, target))