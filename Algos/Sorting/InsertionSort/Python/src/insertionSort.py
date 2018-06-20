def insert(A, pos, value):
    i = pos - 1
    while(i >= 0 and A[i] > value):
        A[i+1] = A[i]
        i -= 1
        A[i+1] = value
    return A

def sort(A):
    for i in range(0,len(A)):
        A = insert(A, i, A[i])
    return A