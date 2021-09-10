#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from collections import defaultdict


class Tree(object):
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


class DeliverTree(object):
    def run(self, nodes: dict = {}) -> Tree:
        depth_map = self.group_by_depth(nodes)
        # 统计相关的状态修改
        root = self.crete(depth_map, root=None, depth=0)
        return root

    def crete(self, depth_map, root=None, depth=0):
        if depth_map.get(depth + 1) == None:
            return
        vals = depth_map.get(depth, [])
        for val in vals:
            if depth == 0 or root is None:
                root = Tree(val)
            root.children = [Tree(i) for i in depth_map.get(depth + 1, [])]
            for node in root.children:
                self.crete(depth_map, node, depth + 1)

            return root

    def group_by_depth(self, nodes: dict = {}) -> dict:
        nodes_depth_dict = {}
        for node in nodes.get("nodes", []):
            depth = node.get("depth")
            if not nodes_depth_dict.get(depth):
                nodes_depth_dict[depth] = []
            nodes_depth_dict[depth].append(node)

        return nodes_depth_dict


def get_json():
    with open("data/106.json", "r") as f:
        data = f.read()
    return data


if __name__ == '__main__':
    data = get_json()
    data = json.loads(data)
    deliver = DeliverTree()
    root = deliver.run(data)
    print(root)
