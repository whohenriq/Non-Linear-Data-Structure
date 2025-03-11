import csv      
from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value, weight):
        self.value = value   
        self.weight = weight 
        self.next = None
        

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def insert(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, v1, v2, weight):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].append((v2, weight))
            self.vertices[v2].append((v1, weight))
            self.edges.append((v1, v2, weight))
            print(f"\nAresta adicionada: {v1} <-> {v2} com peso {weight}")
        else:
            print("Vértices inválidos")

    def display_graph(self):
        print("\nLista de Adjacências:")
        for vertex, neighbors in self.vertices.items():
            print(f"Vértice {vertex}:", end=" ")
            if not neighbors:
                print("(vazio)", end=" ")
            for neighbor, weight in neighbors:
                print(f"-> {neighbor}(peso={weight})", end=" ")
            print("")

    def bfs(self, start, end):
        """
        BFS: Busca o caminho com o menor número de saltos entre 'start' e 'end'.
        Mesmo que o custo (soma dos pesos) não seja o menor, essa busca foca na quantidade de arestas.
        """
        visited = {vertex: False for vertex in self.vertices}
        prev = {vertex: None for vertex in self.vertices}
        queue = Queue()

        visited[start] = True
        queue.put(start)

        while not queue.empty():
            current = queue.get()
            if current == end:
                break
            for neighbor, _ in self.vertices[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    prev[neighbor] = current
                    queue.put(neighbor)

        path = []
        at = end

        if at != start and prev[at] is None:
            print(f"\n[BFS] Não há caminho de {start} para {end}.")
            return

        while at is not None:
            path.append(at)
            if at == start:
                break
            at = prev[at]

        path.reverse()
        print(f"\n[BFS] Menor número de saltos de {start} para {end}: {path}")
        
    def dfs_max_cost(self, start, end):
        """
        DFS - Maior Custo Acumulado:
        Busca recursiva que, dentre todos os caminhos simples (sem ciclos),
        encontra aquele com a maior soma dos pesos.
        Retorna uma tupla (caminho, custo_total) ou imprime uma mensagem se não houver caminho.
        """
        best_cost = float('-inf')
        best_path = None
        visited = {vertex: False for vertex in self.vertices}

        def dfs_util(current, cost, path):
            nonlocal best_cost, best_path
            visited[current] = True

           
            if current == end:
                if cost > best_cost:
                    best_cost = cost
                    best_path = path.copy()
            else:
                for neighbor, weight in self.vertices[current]:
                    if not visited[neighbor]:
                   
                        path.append(neighbor)
                        dfs_util(neighbor, cost + weight, path)
                        path.pop()  # Backtracking

            visited[current] = False

        dfs_util(start, 0, [start])
        if best_path is None:
            print(f"\n[DFS] Não há caminho de {start} para {end}.")
            return None
        else:
            print(f"\n[DFS] Caminho de maior custo acumulado de {start} para {end}: {best_path} | Custo total: {best_cost}")
            return best_path, best_cost


    def load_from_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for source, destination, weight in csv_reader:
                weight = int(weight)  

                if source not in self.vertices:
                    self.insert(source)
                if destination not in self.vertices:
                    self.insert(destination)

                self.add_edge(source, destination, weight)

    def visualize_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()