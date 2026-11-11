'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        bf = AVLTree._balance_factor(node)
        if bf not in (-1, 0, 1):
            return False
        return AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old = node.value
        right = node.right
        new_left = Node(old_value)
        new_left.left = node.left
        node_left.right = right.left
        node.value = right.value
        node.left = new_left
        node.right = right.right
        return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old = node.value
        left = node.left
        new_right = Node(old_value)
        new _right.right = node.right
        node.value = left.value
        node.right = new_right
        node.left = left.left
        return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        self.root = AVLTree._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(value, node.left)
        elif value > node.value:
            node.right = AVLTree._insert(value, node.right)
        return AVLTree._rebalance(node)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        bf = AVLTree._balance_factor(node)
        if bf > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            else:
                node = AVLTree._right_rotate(node)
        elif bf < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            else:
                node = AVLTree._left_rotate(node)
        return node
