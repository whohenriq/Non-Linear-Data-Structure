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
        
    def get_neighbors(self, vertex):
        neighbors = []
        node = self.vertices[vertex]
        while node:
            neighbors.append((node.value, node.weight))
            node = node.next
        return neighbors

    def get_weight(self, v1, v2):
        node = self.vertices[v1]
        while node:
            if node.value == v2:
                return node.weight
            node = node.next
        return float('inf')

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = None

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)

        new_node_v1 = Node(v2, weight)
        new_node_v1.next = self.vertices[v1]
        self.vertices[v1] = new_node_v1

        new_node_v2 = Node(v1, weight)
        new_node_v2.next = self.vertices[v2]
        self.vertices[v2] = new_node_v2

        self.edges.append((v1, v2, weight))
        print(f"\nAresta adicionada: {v1} <-> {v2} com peso {weight}")


    def display_graph(self):
        print("\nLista de Adjacências:")
        for vertex, head in self.vertices.items():
            print(f"Vértice {vertex}:", end=" ")
            if head is None:
                print("(vazio)", end=" ")
            current = head
            while current:
                print(f"-> {current.value}(peso={current.weight})", end=" ")
                current = current.next
            print("")

    def load_from_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for source, destination, weight in csv_reader:
                self.add_edge(source, destination, int(weight))

    def visualize_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()