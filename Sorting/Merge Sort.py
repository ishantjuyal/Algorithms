def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    i = 0
    j = 0
    k = p
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
        
def merge_sort(A, p, r):
    if p < r:
        q = (p+(r-1))//2
        merge_sort(A, p, q)
        merge_sort(A, (q+1), r)
        merge(A, p, q, r)

print("Enter the elements of array you want to sort:")
A = list(map(int, input().split()))
merge_sort(A, 0, len(A) - 1)
print(A)
