#include <iostream>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;
    int bf;
    int height;

    Node(int val = 0, Node* left = nullptr, Node* right = nullptr, int bf = 0, int height = 0) {
        this->val = val;
        this->left = left;
        this->right = right;
        this->bf = bf;
        this->height = height;
    }
};

class AVL {
private:
    Node* root;

    void update(Node* node) {
        int lh = (node->left) ? node->left->height : -1;
        int rh = (node->right) ? node->right->height : -1;

        node->height = 1 + max(lh, rh);
        node->bf = rh - lh;
    }

    Node* rightRotate(Node* node) {
        Node* newP = node->left;
        node->left = newP->right;
        newP->right = node;
        update(node);
        update(newP);
        return newP;
    }

    Node* leftRotate(Node* node) {
        Node* newP = node->right;
        node->right = newP->left;
        newP->left = node;
        update(node);
        update(newP);
        return newP;
    }

    Node* insert(Node* root, int val) {
        if (root == nullptr) {
            return new Node(val);
        }
        else if (root->val == val) {
            return nullptr;
        }
        else if (root->val < val) {
            root->right = insert(root->right, val);
        }
        else {
            root->left = insert(root->left, val);
        }
        update(root);
        return balance(root);
    }

    Node* remove(Node* root, int val) {
        if (root == nullptr) {
            return root;
        }
        else if (root->val > val) {
            root->left = remove(root->left, val);
        }
        else if (root->val < val) {
            root->right = remove(root->right, val);
        }
        else {
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }
            else {
                Node* successor = root->right;
                while (successor->left) {
                    successor = successor->left;
                }
                root->val = successor->val;
                root->right = remove(root->right, root->val);
            }
        }
        update(root);
        return balance(root);
    }

    Node* balance(Node* node) {
        if (node->bf == -2) {
            if (node->left->bf <= 0) {
                return rightRotate(node);
            }
            else {
                node->left = leftRotate(node->left);
                return rightRotate(node);
            }
        }
        else if (node->bf == 2) {
            if (node->right->bf >= 0) {
                return leftRotate(node);
            }
            else {
                node->right = rightRotate(node->right);
                return leftRotate(node);
            }
        }
        return node;
    }

public:
    AVL() {
        root = nullptr;
    }

    void insert(int val) {
        root = insert(root, val);
    }

    void remove(int val) {
        root = remove(root, val);
    }

    void drawAVLTree(Node* node, int level = 0, int indent = 4) {
        if (node == nullptr) {
            return;
        }
        drawAVLTree(node->right, level + 1, indent);
        cout << string(level * indent, ' ') << node->val << endl;
        drawAVLTree(node->left, level + 1, indent);
    }

    void drawAVLTree() {
        drawAVLTree(root);
    }
};

int main() {
    AVL avl;
    for (int i = 0; i < 16; i++) {
        avl.insert(i);
    }
    avl.drawAVLTree();

    avl.remove(1);
    avl.remove(2);
    avl.remove(3);
    avl.remove(0);
    avl.remove(9);
    cout << "\n\n";
    avl.drawAVLTree();

    return 0;
}
