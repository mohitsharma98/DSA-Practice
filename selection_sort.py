def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        mini = i
        for j in range(i+1, n):
            if (a[j]<a[mini]):
                mini = j
            a[i], a[mini] = a[mini], a[i]
    return a

if __name__ == "__main__":
    a = [3,2,5,7,3,1,6,9,4]
    print(selection_sort(a))