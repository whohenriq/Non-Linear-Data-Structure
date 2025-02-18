#include <iostream>
using namespace std;

class Node
{
public:
    int vertex;
    Node *next;
    Node(int v) : vertex(v), next(nullptr) {}
};

class AdjacencyList
{
public:
    Node *head;
    AdjacencyList() : head(nullptr) {}

    void addNode(int v)
    {
        Node *newNode = new Node(v);
        newNode->next = head;
        head = newNode;
    }
};

class Graph
{
private:
    int Vertices;
    AdjacencyList *adjList;

public:
    Graph(int vertices)
    {

        Vertices = vertices;
        adjList = new AdjacencyList[Vertices];
    }

    bool isValidVertex(int vertice)
    {
        return vertice >= 0 && vertice < Vertices;
    }

    void addEdge(int v1, int v2)
    {
        if (isValidVertex(v1) && isValidVertex(v2))
        {
            adjList[v1].addNode(v2);
            adjList[v2].addNode(v1);
            cout << "\nAresta adicionada: " << v1 << " <-> " << v2 << endl;
        }
        else
        {
            cout << "Vertices invalidos\n";
        }
    }

    void display()
    {
        cout << "\nLista de Adjacencias:";
        for (int i = 0; i < Vertices; i++)
        {
            cout << "\nVertice:" << i << " -> ";
            Node *current = adjList[i].head;
            if (!current)
            {
                cout << "(vazio)";
            }
            while (current)
            {
                cout << current->vertex;
                if (current->next)
                    cout << " -> ";
                current = current->next;
            }
            cout << "\n";
        }
    }
};

int main()
{
    Graph graph(5);
    graph.display();

    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(0, 2);
    graph.addEdge(2, 4);
    graph.addEdge(3, 4);
    graph.addEdge(4, 2);

    graph.display();

    return 0;
}