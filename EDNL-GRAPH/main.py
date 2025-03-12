from graph import Graph
from functions import bfs, dfs

def main():
    graph = Graph()
    
    graph.load_from_csv("graph.csv")
    graph.display_graph()
    
    start = 'A'
    end = 'I'
    
    print(bfs(graph, start, end))
    print(dfs(graph, start, end))
    
    graph.visualize_graph()

if __name__ == "__main__":
    main()