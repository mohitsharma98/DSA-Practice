def partition(a,l,h):
    pivot = a[l]
    i = l
    j = h

    while(i<j):
        while(a[i]<=pivot):
            i+=1
        while(a[j]>pivot):
            j-=1

        if (i<j):
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(a,l,h):
    if(l<h):
        j = partition(a,l,h)

        quick_sort(a, l, j-1)
        quick_sort(a, j+1, h)
    return a

a = [3,2,5,7,3,1,6,9,4]
l = 0
h = len(a)-1

print(quick_sort(a,l,h))