#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' python递归遍历实现二叉树 '''

class Node(object):
    ''' 节点 坐标以及左右子树 '''
    def __init__(self, index):
        self.index = index
        self.left_child = None
        self.right_child = None

class BinaryTree(object):
    ''' 二叉树 根节点 三种递归遍历查找方法 '''
    def __init__(self, root):
        ''' 设置根节点 '''
        self.root = root

    def pre_travel(self, node):
        ''' 前序递归遍历查找 根左右 '''
        if not node:
            return
        print(node.index)
        self.pre_travel(node.left_child)
        self.pre_travel(node.right_child)
    
    def mid_travel(self, node):
        ''' 中序递归遍历查找 左根右 '''
        if not node:
            return
        self.mid_travel(node.left_child)
        print(node.index)
        self.mid_travel(node.right_child)
    
    def post_travel(self, node):
        ''' 后序递归遍历查找 左右根 '''
        if not node:
            return
        self.post_travel(node.left_child)
        self.post_travel(node.right_child)
        print(node.index)

node_dict = {}
for i in range(1, 11):
    node_dict[i] = Node(i)
node_dict[1].left_child = node_dict[2]
node_dict[1].right_child = node_dict[3]
node_dict[2].left_child = node_dict[4]
node_dict[3].left_child = node_dict[5]
node_dict[3].right_child = node_dict[6]
node_dict[4].left_child = node_dict[7]
node_dict[4].right_child = node_dict[8]
node_dict[5].right_child = node_dict[9]
node_dict[6].left_child = node_dict[10]

tree = BinaryTree(node_dict[1])
print('前序递归遍历输出:')
tree.pre_travel(tree.root)
print('中序递归遍历输出:')
tree.mid_travel(tree.root)
print('后序递归遍历输出:')
tree.post_travel(tree.root)
