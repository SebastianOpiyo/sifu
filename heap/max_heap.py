class MaxHeap:
    '''
    A Max-Heap is a complete binary tree in which the value in each internal
    node is greater than or equal to the values in the children of that node.
    '''

    def parent(self, pos):
        return (pos - 1) // 2

    def leftChild(self, pos):
        return (2 * pos) + 1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, A, pos):
        size = len(A)
        return pos <= size and pos >= (size // 2)

    def maxHeapify(self, A, n, i):
        largest = i
        left_child = self.leftChild(i)
        right_child = self.rightChild(i)

        if left_child < n and A[i] < A[left_child]:
            largest = left_child

        if right_child < n and A[largest] < A[right_child]:
            largest = right_child

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.maxHeapify(A, n, largest)   # Heapify the sub heap

    def build_max_heap(self, A):
        # O(n) time
        size = len(A)
        no_leaf_nodes_max_idx = (size // 2) - 1

        for i in range(no_leaf_nodes_max_idx, -1, -1):
            self.maxHeapify(A, size, i)

    def insertNode(self, A, num):
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        size = len(A)
        if not size:
            A.append(num)
        else:
            A.append(num)
            new_size = len(A)
            no_leaf_nodes_max_idx = (new_size // 2) - 1

            for i in range(no_leaf_nodes_max_idx, -1, -1):
                self.maxHeapify(A, new_size, i)

    def deleteNode(self, A):  # extractMax
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        size = len(A)

        # Swap first and last element
        A[0], A[size-1] = A[size-1], A[0]

        popped = A.pop(size-1)

        new_size = len(A)
        no_leaf_nodes_max_idx = (new_size // 2) - 1
        for i in range(no_leaf_nodes_max_idx, -1, -1):
            self.maxHeapify(A, new_size, i)

        return popped

    def heapSort(self, A):
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        n = len(A)

        # Build a maxheap.
        self.build_max_heap(A)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self.maxHeapify(A, i, 0)


# -------------------------------

mh = MaxHeap()

arr = [3, 12, 11, 13, 5, 6, 7]
sorted_arr = sorted(arr)
mh.heapSort(arr)
assert arr == sorted_arr

# -------------------------------

A = []
mh.insertNode(A, 3)
mh.insertNode(A, 1)
mh.insertNode(A, 4)
mh.insertNode(A, 9)
mh.insertNode(A, 5)
mh.insertNode(A, 2)

assert A == [9, 5, 3, 1, 4, 2]

# -------------------------------

assert mh.deleteNode(A) == 9
assert A == [5, 4, 3, 1, 2]