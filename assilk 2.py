N = int(input())
L = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    query_type = input()
    if query_type == "Insert":
        index, value = map(int, input().split())
        L.insert(index, value)
    elif query_type == "Delete":
        index = int(input())
        del L[index]

for i in L:
    print(i, " ")
