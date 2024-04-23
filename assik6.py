from heapq import heapify, heappush, heappop

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 35)
heappush(heap, 19)
heappush(heap, 7)
heappush(heap, 21)
heappush(heap, 15)
heappush(heap, 6)
heappush(heap, 22)
heappush(heap, 9)
print((heap[0]))

for i in heap:
    print(i, end = ' ')
print("\n")

element = heappop(heap)

for i in heap:
    print(i, end = ' ')