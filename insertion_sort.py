def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        value = a[i]
        hole = i

        while(hole!=0 and a[hole-1]>value):
            a[hole] = a[hole-1]
            hole-=1

        a[hole] = value

    return a

if __name__ == "__main__":
    a = [3,2,5,7,3,1,6,9,4]
    print(insertion_sort(a))