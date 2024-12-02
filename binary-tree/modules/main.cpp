#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;
};

Node *getNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->left, NULL;
    newNode->right = NULL;

    return newNode;
};

Node *insert(Node *root, int data)
{
    if (root == NULL)
    {
        root = getNewNode(data);
        return root;
    }
    else if (data <= root->data)
    {
        root->left = insert(root->left, data);
    }
    else
    {
        root->right = insert(root->right, data);
    }

    return root;
};

bool searchNode(Node *root, int data)
{
    if (root == NULL)
    {
        return false;
    }

    else if (root->data == data)
    {
        return true;
    }
    else if (data <= root->data)
    {
        return searchNode(root->left, data);
    }
    else
    {
        return searchNode(root->right, data);
    }
};

int getHight(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    return 1 + max(getHight(root->left), getHight(root->right));
}

int countNodes(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}

int countLeaves(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL && root->right == NULL)
    {
        return 1;
    }
    return countLeaves(root->left) + countLeaves(root->right);
}

void display_tree(Node *root, int spaces = 0)
{
    if (root == NULL)
    {
        return;
    }

    spaces += 10;

    display_tree(root->right, spaces);
    cout << "\n";

    for (int i = 0; i < spaces; i++)
    {
        cout << " ";
    }

    cout << root->data << endl;

    display_tree(root->left, spaces);
}

int main()
{
    Node *root = NULL;

    root = insert(root, 100);
    root = insert(root, 50);
    root = insert(root, 200);
    root = insert(root, 70);
    root = insert(root, 140);
    root = insert(root, 30);
    root = insert(root, 350);
    root = insert(root, 117);
    root = insert(root, 400);
    root = insert(root, 42);
    root = insert(root, 80);
    root = insert(root, 65);

    cout << "Height binary: " << getHight(root) << endl;

    cout << "Total number of nodes: " << countNodes(root) << endl;
    cout << "Total number of leaves: " << countLeaves(root) << endl;

    int number;
    cout << "Enter number be searched\n";
    cin >> number;

    if (searchNode(root, number) == true)
    {
        cout << "Found!!!" << endl;
    }
    else
    {
        cout << "Not found." << endl;
    }

    display_tree(root);

    return 0;
}