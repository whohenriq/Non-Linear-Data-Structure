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

def tsp_dfs(graph: Graph, origin, current, visited_cities, current_cost, current_path, best_cost, best_path):

    if len(visited_cities) == len(graph.vertices):
        total_cost = current_cost + get_weight(graph, current, origin)
        if total_cost < best_cost:
            best_cost = total_cost
            best_path = current_path + [origin]
        return best_cost, best_path

    for neighbor, cost in get_neighbors(graph, current):
        if neighbor not in visited_cities:
            visited_cities.add(neighbor)
            current_path.append(neighbor)
            best_cost, best_path = tsp_dfs(graph, origin, neighbor, visited_cities, current_cost + cost, current_path, best_cost, best_path)
            visited_cities.remove(neighbor)
            current_path.pop()

    return best_cost, best_path


def get_weight(graph: Graph, v1, v2):
    node = graph.vertices[v1]
    while node:
        if node.value == v2:
            return node.weight
        node = node.next
    return float('inf')

def get_neighbors(graph: Graph, vertice):
    neighbors = []
    node = graph.vertices[vertice]
    while node:
        neighbors.append((node.value, node.weight))
        node = node.next
    return neighbors
