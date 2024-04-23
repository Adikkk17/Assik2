N = int(input())
N > 1 and N <1000
Array = [ ]
#Array = shelves
remove_disks = []
for i in range(N):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        Array.insert(0, operation[1])
    elif operation[0] == 2:
        Array.append(operation[1])
    elif operation[0] == 3:
        remove_disks.append(Array.pop())
    elif operation[0] == 4:
        remove_disks.append(Array.pop(0))

print(" ".join(map(str, remove_disks)))
