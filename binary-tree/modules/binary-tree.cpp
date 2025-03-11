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

Node *min(Node *root)
{
    Node *currentRoot = root;
    while (currentRoot->left != nullptr)
    {
        currentRoot = currentRoot->left;
    }

    return currentRoot;
}

Node *max(Node *root)
{
    Node *currentRoot = root;
    while (currentRoot->right != nullptr)
    {
        currentRoot = currentRoot->right;
    }

    return currentRoot;
}

void visit(Node *node)
{
    cout << node->data << " " << endl;
}

void preOrder(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        return;
    }

    visit(currentRoot);
    preOrder(currentRoot->left);
    preOrder(currentRoot->right);
}

void inOrder(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        return;
    }

    inOrder(currentRoot->left);
    visit(currentRoot);
    inOrder(currentRoot->right);
}

void postOrder(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        return;
    }

    postOrder(currentRoot->left);
    postOrder(currentRoot->right);
    visit(currentRoot);
}

Node *searchNode(Node *root, int valueToFind)
{
    Node *currentRoot = root;
    Node *findNode = nullptr;

    while (currentRoot != nullptr)
    {
        findNode = currentRoot;
        if (valueToFind < currentRoot->data)
        {
            currentRoot = currentRoot->left;
        }
        else
        {
            currentRoot = currentRoot->right;
        }
    }
    return findNode;
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

/*
Caso 1: remove nó folha
Caso 2: remove nó com apenas um filho
Caso 3: Nó com dois filhos, buscar valor e buscar sucessor, deletar sucessor
*/
Node *removeNode(Node *currentRoot, int value)
{
    if (currentRoot == nullptr)
    {
        return nullptr;
    }

    if (value < currentRoot->data)
    {
        currentRoot->left = removeNode(currentRoot->left, value);
    }
    else if (value > currentRoot->data)
    {
        currentRoot->right = removeNode(currentRoot->right, value);
    }
    else
    {
        if (currentRoot->left != nullptr && currentRoot->right != nullptr)
        {
            Node *minimun = min(currentRoot->right);
            currentRoot->data = minimun->data;
            currentRoot->right = removeNode(currentRoot->right, minimun->data);
        }
        else
        {
            Node *aux = currentRoot;
            if (currentRoot->left != nullptr)
            {
                currentRoot = currentRoot->left;
            }
            else
            {
                currentRoot = currentRoot->right;
            }

            delete aux;
        }
    }
    return currentRoot;
}

int countTotalNodes(Node *currentRoot)
{
    if (currentRoot == nullptr)
    {
        return 0;
    }

    return 1 + countTotalNodes(currentRoot->left) + countTotalNodes(currentRoot->right);
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

    return countLeafNodes(currentRoot->left) + countLeafNodes(currentRoot->right);
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
    Node *root = nullptr;
    int choice, value;
    Node *valueMin, *valueMax;

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

    valueMin = min(root);
    cout << valueMin->data << endl;

    valueMax = max(root);
    cout << valueMax->data << endl;

    do
    {
        cout << "\nMenu de Operações:\n";
        cout << "1. Inserir nó\n";
        cout << "2. Remover nó\n";
        cout << "3. Buscar valor\n";
        cout << "4. Exibir árvore\n";
        cout << "5. Percurso In-Order\n";
        cout << "6. Percurso Pre-Order\n";
        cout << "7. Percurso Post-Order\n";
        cout << "8. Contar total de nós\n";
        cout << "9. Contar folhas\n";
        cout << "10. Sair\n";
        cout << "Escolha uma opção: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "\nDigite o valor para inserir: ";
            cin >> value;
            root = insertNode(root, value);
            cout << "\nValor inserido com sucesso!\n";
            break;

        case 2:
            cout << "\nDigite o valor para remover: ";
            cin >> value;
            root = removeNode(root, value);
            cout << "\nValor removido (se existia)!\n";
            break;

        case 3:
            cout << "\nDigite o valor para buscar: ";
            cin >> value;
            if (searchNode(root, value))
                cout << "\nValor encontrado na árvore.\n";
            else
                cout << "\nValor não encontrado.\n";
            break;

        case 4:
            cout << "\nÁrvore Binária:\n";
            displayTree(root);
            break;

        case 5:
            cout << "\nPercurso Pre-Order:";
            preOrder(root);
            cout << endl;
            break;

        case 6:
            cout << "\nPercurso In-Order : ";
            inOrder(root);
            cout << endl;
            break;

        case 7:
            cout << "\nPercurso Post-Order: ";
            postOrder(root);
            cout << endl;
            break;

        case 8:
            cout << "\nNúmero total de nós: " << countTotalNodes(root) << endl;
            break;

        case 9:
            cout << "\nNúmero total de folhas: " << countLeafNodes(root) << endl;
            break;

        case 10:
            cout << "\nSaindo do programa.\n";
            break;

        default:
            cout << "\nOpção inválida. Tente novamente.\n";
        }
    } while (choice != 10);

    return 0;
}