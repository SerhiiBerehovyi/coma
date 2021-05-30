class Node:
    """
    simple class to represent a node of graph
    :successors: an array with nodes, that can be
                 reached directly from this node
    :names: 	 name of node
    :color:		 color of node. "white" by default
    """
    def __init__(self):
        self.successors = []
        self.name = ""
        self.color = "white"


def top_order(G):
    """
    sorts graph G in topological order

    :param G: Graph in form of an array with Node's
    :return: an array with names of sorted Node's
    """

    def toNames(arr):
        """
        simple help-function to convert all nodes in array arr
        to array with names of apropriate nodes

        :param arr: array of nodes
        :return: array of names of nodes
        """
        names = []
        for a in arr:
            names.append(a.name)
        return names

    def visit(node):
        """
        visits @node and it's successors to check on existing of topological order
        and adds this nodes to array res

        :param node: index of Node in array G
        :return: True, if there is an Cycle in G (there is no topological order)
                 False, if not
        """
        if nodes[node] == not_visited:
            nodes[node] = inprocess
            for suc in G[node].successors:
                if visit(G.index(suc)):
                    return True

            nodes[node] = visited
            res.append(G[node])
            return False
        elif nodes[node] == inprocess:
            return True
        else:
            return False

    res = []
    if len(G) == 0:
        return res
    # Flags for nodes-array
    # inprocess means that visit-function was called for this node
    not_visited, inprocess, visited = 0, 1, 2
    # an array with flags for every node of G
    nodes = [not_visited] * len(G)

    for node in range(len(G)):
        if visit(node):
            return [-1]

    res.reverse()
    return toNames(res)
