a = [3,2,5,7,3,1,6,9,4]

def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)-1-i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubble_sort(a))