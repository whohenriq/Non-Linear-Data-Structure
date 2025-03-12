from graph import Graph
from functions import tsp_dfs

def main():
    graph = Graph()
    
    graph.load_from_csv("graph.csv")
    graph.display_graph()
    
    start = 'A' 
    best_cost = float('inf')
    best_path = []

    visited_cities = set([start])
    current_path = [start]
    
    best_cost, best_path = tsp_dfs(graph, start, start, visited_cities, 0, current_path, best_cost, best_path)

    print("\nMelhor caminho encontrado: ", best_path)
    print("Custo do melhor caminho: ", best_cost)

    graph.visualize_graph()

if __name__ == "__main__":
    main()