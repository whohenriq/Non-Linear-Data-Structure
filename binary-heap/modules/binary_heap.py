class BinaryHeap:
    """
    Binary Heap é uma estrutura de dados que organiza os elementos em uma "espécie" de árvore e também uma das principais implementações para fila de prioridade. Essa estrutura é utilizado no algoritmo de ordenação HeapSort, 

    Uma Binary Heap sempre deve ter uma das duas configurações que são: MIN_HEAP ou MAX_HEAP

    MIN_HEAP: Em uma arvore para qualquer nó os elementos filhos tem valor maior do que o elemento pai.

    MAX_HEAP: Em uma arvore para cada nó, o elemento pai tem valor maior do que os elementos filhos.
    """

    def __init__(self) -> None:
        self.heap = []

    def __left_side(self, nodeIndex: int) -> int:
        result = (2 * nodeIndex) + 1
        if result < len(self.heap):
            return result
        return -1   
    
    def __right_side(self, nodeIndex: int) -> int:
        result = (2 * nodeIndex) + 2
        if result < len(self.heap):
            return result
        return -1
    
    def __verify_parent(self, nodeIndex: int) -> int:
        if nodeIndex == 0:
            return -1
        return (nodeIndex - 1) // 2
    
    def __is_bigger(self, firstIndex: int, secondIndex: int) -> bool:
        # Comparação entre dois valores na lista heap
        if secondIndex == -1:  # Índice -1 significa que não há pai
            return False
        return self.heap[firstIndex] > self.heap[secondIndex]
    
    def __swap(self, indexA: int, indexB: int) -> None:
        self.heap[indexA], self.heap[indexB] = self.heap[indexB], self.heap[indexA]

    def heapify_down(self, index: int):
        largest = index
        left = self.__left_side(index)
        right = self.__right_side(index)

        if left != -1 and self.heap[left] > self.heap[largest]:
            largest = left

        if right != -1 and self.heap[right] > self.heap[largest]:
            largest = right

        # Troca e continua o heapify-down se o maior não for o índice atual
        if largest != index:
            self.__swap(index, largest)
            self.__heapify_down(largest)

    def heapify_up(self, index: int):
        currentIndex = index
        parentIndex = self.verify_parent(currentIndex)

        # Subir enquanto o nó é maior que o pai (para MAX_HEAP)
        while parentIndex != -1 and self.is_bigger(currentIndex, parentIndex):
            self.swap(currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = self.verify_parent(currentIndex)

    def insert(self, newNode: int) -> None: 
        self.heap.append(newNode)
        currentIndex = len(self.heap) - 1
        parentIndex = self.verify_parent(currentIndex)

        # Reorganiza o heap subindo o novo nó até a posição correta
        while parentIndex != -1 and self.is_bigger(currentIndex, parentIndex):
            self.swap(currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = self.verify_parent(currentIndex)

    def remove(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty!")
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.heapify_down(0)

        return root

    def change_priority(self, nodeIndex: int, newPriority: int):
        if (nodeIndex < 0 or nodeIndex >= len(self.heap)):
            raise IndexError("Index out of bounds")
        
        oldPriority = self.heap[nodeIndex]
        self.heap[nodeIndex] = newPriority

        print("Teste", self.heap)

        if (newPriority > oldPriority):
            self.heapify_up(nodeIndex)

        if (newPriority < oldPriority):
            self.heapify_down(nodeIndex)
        
    def get_high_priority(self) -> int:
        if not self.heap:
            return None
        return self.heap[0]

    def display_heap(self):
        print(f"{self.heap}")

    def heap_sort(self) -> int:
        pass
