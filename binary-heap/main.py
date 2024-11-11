from modules.binary_heap import BinaryHeap

def main():
    heap = BinaryHeap()
    print(f"\nHeap inicial: ", heap.heap)

    elements_to_insert = [10, 5, 20, 1, 15, 30, 25]
    print(f"\nInserindo elementos:", elements_to_insert)
    
    for element in elements_to_insert:
        heap.insert(element)
        print(f"Após inserir {element}: {heap.heap}")

    print(f"\nEstrutura final do heap:", heap.heap)
    print(f"\nElemento de alta prioridade:", heap.get_high_priority())

    print(f"\nAlterar a prioridade do índice 3 para 50:", heap.change_priority(3, 50))
    print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    print(f"\nEstrutura final do heap:", heap.heap)
    print(f"\nAlterar a prioridade do índice 1 para 8:", heap.change_priority(1, 8))
    print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    print(f"\nEstrutura final do heap:", heap.heap)



    # heap.remove()
    # print("Heap após remover elemento de alta prioridade:", heap.heap)
    # print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    # heap.remove()
    # print("Heap após remover elemento de alta prioridade:", heap.heap)
    # print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    # heap.remove()
    # print("Heap após remover elemento de alta prioridade:", heap.heap)
    # print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    # heap.remove()
    # print("Heap após remover elemento de alta prioridade:", heap.heap)
    # print(f"\nElemento de alta prioridade:", heap.get_high_priority())
    # heap.remove()
    # print("Heap após remover elemento de alta prioridade:", heap.heap)
    
if __name__ == "__main__":
    main()
