#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.children = []  # 这里必须是一个有序，所以选择的是数组


class Tree(object):

    def __init__(self, states_end):
        self.states_end = states_end
        self.end_nodes = []

    # 创建N叉树
    def create(self, val, data):
        # 终止条件
        if not data.get(val):
            return None

        root = Node(val=val)

        for i in data.get(val, []):
            # 这里进行剪枝的操作
            node = self.create(val=i, data=data)
            root.children.append(node)

        return root

    def show(self, root):
        if not root:
            return
        print(root.val)
        if root and not root.children:
            self.end_nodes.append(root.val)
        for i in root.children:
            self.show(i)

        return self.end_nodes
