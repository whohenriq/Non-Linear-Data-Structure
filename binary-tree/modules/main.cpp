#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;
};

Node *createNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->left, nullptr;
    newNode->right = nullptr;
    return newNode;
};

Node *insertNode(Node *currentRoot, int valueToInsert)
{
    if (currentRoot == nullptr)
    {
        Node *newNode = createNewNode(valueToInsert);
        return newNode;
    }

    if (valueToInsert <= currentRoot->data)
    {
        currentRoot->left = insertNode(currentRoot->left, valueToInsert);
    }
    else
    {
        currentRoot->right = insertNode(currentRoot->right, valueToInsert);
    }

    return currentRoot;
};

bool searchNode(Node *currentRoot, int valueToFind)
{
    if (currentRoot == nullptr)
    {
        return false;
    }

    if (currentRoot->data == valueToFind)
    {
        return true;
    }

    if (valueToFind <= currentRoot->data)
    {
        return searchNode(currentRoot->left, valueToFind);
    }

    else
    {
        return searchNode(currentRoot->right, valueToFind);
    }
};

int countTotalNodes(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        return 0;
    }

    int leftNodeCount = countTotalNodes(currentRoot->left);
    int rightNodeCount = countTotalNodes(currentRoot->right);

    return 1 + leftNodeCount + rightNodeCount;
}

int countLeafNodes(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        // Não possui nenhuma folha na subárvore
        return 0;
    }

    if (currentRoot->left == nullptr && currentRoot->right == nullptr)
    {
        // É um nó folha
        return 1;
    }

    int leftLeafCount = countLeafNodes(currentRoot->left);
    int rightLeafCount = countLeafNodes(currentRoot->right);

    return leftLeafCount + rightLeafCount;
}

void displayTree(Node *currentRoot, int indent = 0)
{
    if (currentRoot == nullptr)
    {
        // Árvore vazia. 0
        return;
    }

    indent += 10;

    displayTree(currentRoot->right, indent);
    cout << string(indent, ' ') << currentRoot->data << endl;
    displayTree(currentRoot->left, indent);
}

int main()
{
    Node *root = NULL;

    root = insertNode(root, 100);
    root = insertNode(root, 50);
    root = insertNode(root, 200);
    root = insertNode(root, 70);
    root = insertNode(root, 140);
    root = insertNode(root, 30);
    root = insertNode(root, 350);
    root = insertNode(root, 117);
    root = insertNode(root, 400);
    root = insertNode(root, 42);
    root = insertNode(root, 80);
    root = insertNode(root, 65);

    cout << "Árvore Binária:\n";
    displayTree(root);

    int valueToSearch;
    cout << "\nDigite um valor para buscar: ";
    cin >> valueToSearch;

    if (searchNode(root, valueToSearch))
    {
        cout << "Valor encontrado na árvore.\n";
    }
    else
    {
        cout << "Valor não encontrado na árvore.\n";
    }

    cout << "Número total de nós: " << countTotalNodes(root) << endl;
    cout << "Número total de folhas: " << countLeafNodes(root) << endl;

    return 0;
}