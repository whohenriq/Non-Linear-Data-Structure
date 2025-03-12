from queue import Queue
from graph import Graph

def bfs(graph: Graph, start, end):
    """
    Busca em Largura (BFS):
    -----------------------
    Encontra o caminho com o menor número de saltos (arestas) entre os vértices 'start' e 'end'.
    
    Parâmetros:
    - start: Vértice de início.
    - end: Vértice de destino.
    
    Funcionamento:
    - Utiliza uma fila para explorar os vértices de forma sequencial.
    - Utiliza um dicionário 'visited' para controlar os vértices já visitados.
    - Utiliza um dicionário 'prev' para registrar o vértice anterior de cada vértice visitado,
        permitindo a reconstrução do caminho.
        
    Nota:
    - Esse método foca na quantidade de arestas, não necessariamente no menor custo (soma dos pesos).
    """
    if start not in graph.vertices or end not in graph.vertices:
        return "Vértices inválidos"

    queue = Queue()
    visited = {vertice: False for vertice in graph.vertices}
    distance = {vertice: float() for vertice in graph.vertices}

    queue.put(start)
    visited[start] = True
    distance[start] = 0

    while not queue.empty():
        current = queue.get()

        if current == end:
            return f"[BFS] Menor número de saltos de {start} para {end}: {distance[current]}"

        temp = graph.vertices[current]
        while temp:
            neighbor = temp.value
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.put(neighbor)
            temp = temp.next

    return f"[BFS] Nenhum caminho encontrado de {start} para {end}"

def dfs(graph: Graph, start, end):
    """
    Busca em Profundidade (DFS) para Maior Custo Acumulado:
    ---------------------------------------------------------
    Explora todos os caminhos simples (sem ciclos) entre 'start' e 'end' e retorna aquele
    com o maior custo acumulado (soma dos pesos das arestas).
    
    Parâmetros:
    - start: Vértice de início.
    - end: Vértice de destino.
    
    Funcionamento:
    - Utiliza uma função auxiliar recursiva 'dfs_util' para explorar todos os caminhos.
    - Controla os vértices visitados para evitar ciclos.
    - Aplica a técnica de backtracking: após explorar um caminho, remove o último vértice
        para testar outros caminhos possíveis.
        
    Retorno:
    - Se existir um caminho, retorna uma tupla (caminho, custo_total).
    - Caso contrário, informa que não há caminho entre os vértices.
    """
    if start not in graph.vertices or end not in graph.vertices:
        return "Vértices inválidos"

    best_path = None
    max_cost = float() 
    visited = set()

    def dfs_recursive(current, current_cost, path):
        nonlocal best_path, max_cost
        if current == end:
            if current_cost > max_cost:
                max_cost = current_cost
                best_path = path[:]
            return

        visited.add(current)
        
        temp = graph.vertices[current]
        while temp:
            neighbor, weight = temp.value, temp.weight
            if neighbor not in visited:
                # Passando o peso da aresta para o cálculo do custo
                dfs_recursive(neighbor, current_cost + weight, path + [neighbor])
            temp = temp.next
        
        visited.remove(current)  # Backtracking

    dfs_recursive(start, 0, [start])

    if best_path:
        return f"[DFS] Caminho de maior custo acumulado de {start} para {end}: {best_path} | Custo total: {max_cost}"
    else:
        return f"[DFS] Nenhum caminho encontrado de {start} para {end}"

