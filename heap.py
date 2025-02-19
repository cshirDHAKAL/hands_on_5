class MinHeap:
    def __init__(self, data=None):
        self.heap = data if data else []
        if self.heap:
            self.build_min_heap()

    def parent(self, index):
        return (index - 1) >> 1  # Bitwise equivalent to (index - 1) // 2

    def left(self, index):
        return (index << 1) + 1  # Bitwise equivalent to 2 * index + 1

    def right(self, index):
        return (index << 1) + 2  # Bitwise equivalent to 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify(smallest)

    def build_min_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    def push(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


# Demonstration of functionality
if __name__ == "__main__":
    data = [64, 4, 82, 1, 33, 63, 81]
    heap = MinHeap(data)
    print("Initial min heap:", heap)

    heap.push(2)
    print("Heap after inserting 2:", heap)

    min_element = heap.pop()
    print("Extracted min element:", min_element)
    print("Heap after extracting min:", heap)

    heap.push(0)
    print("Heap after inserting 0:", heap)

    while heap.heap:
        print("Extracting:", heap.pop(), "| Heap now:", heap)
