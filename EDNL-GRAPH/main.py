from graph import Graph

def main():
    graph = Graph()
    
    graph.load_from_csv("graph.csv")
    graph.display_graph()
    
    start = 'A'
    end = 'I'
    graph.bfs(start, end)
    graph.dfs_max_cost(start, end)
    
    graph.visualize_graph()

if __name__ == "__main__":
    main()