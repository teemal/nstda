#!/usr/bin/env python
#
#
import os,sys, basic_graph
def calculate_components(g):
    # Creates a table of components via a breadth-first search 
    component_table = {}
    unfinished_nodes = {}
    for i in g.nodes.keys():
        unfinished_nodes[i] = 1 
        node_list = [g.nodes.keys()[0]] 
        component_index = 1
    while node_list != []:
        current_node = node_list[0]
        del node_list[0]
        del unfinished_nodes[current_node] 
        for i in g.neighbors(current_node):
            component_table[i] = component_index
            node_list.insert(0, i)
        if node_list == [] and len(unfinished_nodes) > 0:
            node_list = [unfinished_nodes.keys()[0]] 
    return component_table