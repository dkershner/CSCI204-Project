class Heap:
    def parent(self, heap, index):
        if len(heap) < index:
            return
        elif heap[0] == None:
            return heap[index // 2]
        else:
            return heap[(index-1) // 2]

    def leftChild(self, heap, index):
        if len(heap) < index:
            return
        elif heap[0] == None:
            return heap[2 * index]
        else:
            return heap[(2 * index) + 1]

    def rightChild(self, heap, index):
        if len(heap) < index:
            return
        elif heap[0] == None:
            return heap[(2 * index) + 1]
        else:
            return heap[(2 * index) + 2]

class MinHeap(Heap):
    def fixUp(heap, node):
        index = heap.index(node)
        parent = parent(heap, index)
        parentIndex = heap.index(parent)
        if parent == None:
            return heap
        elif parent.value < node.value:
            heap[parentIndex] = node
            heap[index] = parent
            return fixUp(heap, node)
        return heap

    def heapAdd(heap, node):
        if heap == []:
            heap.append(None)
        heap.append(node)
        heap = fixUp(heap, node)
        return heap

    def fixDown(heap, index = 1):
        if heap == []:
            return
        left = leftChild(heap, index)
        leftIndex = heap.index(left)
        right = rightChild(heap, index)
        rightIndex = heap.index(right)
        if left.value > heap[index].value:
            heap[leftIndex] = heap[index]
            heap[index] = left
            return fixDown(heap, leftIndex)
        elif right.value > heap[index].value:
            heap[rightIndex] = heap[index]
            heap[index] = right
            return fixDown(heap, rightIndex)
        return heap

    def heapRemove(heap):
        t = heap[1]
        heap[1] = heap[-1]
        del heap[-1]
        heap = fixDown(heap)
        return t, heap

class MaxHeap(Heap):
    def fixUp(self, heap, node):
        index = heap.index(node)
        parent = self.parent(heap, index)
        parentIndex = heap.index(parent)
        if parent == None:
            return heap
        elif parent.value > node.value:
            heap[parentIndex] = node
            heap[index] = parent
            return self.fixUp(heap, node)
        return heap

    def heapAdd(self, heap, node):
        if heap == []:
            heap.append(None)
        heap.append(node)
        heap = self.fixUp(heap, node)
        return heap

    def fixDown(self, heap, index = 1):
        if heap == []:
            return
        left = self.leftChild(heap, index)
        leftIndex = heap.index(left)
        right = self.rightChild(heap, index)
        rightIndex = heap.index(right)
        if left.value < heap[index].value:
            heap[leftIndex] = heap[index]
            heap[index] = left
            return self.fixDown(heap, leftIndex)
        elif right.value < heap[index].value:
            heap[rightIndex] = heap[index]
            heap[index] = right
            return self.fixDown(heap, rightIndex)
        return heap

    def heapRemove(self, heap):
        t = heap[1]
        heap[1] = heap[-1]
        del heap[-1]
        heap = self.fixDown(heap)
        return t, heap
class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
