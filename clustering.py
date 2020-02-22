def calculate_clustering_coefficients(g):
# Clustering coefficient for a node is the
# fraction of its neighbors who are also neighbors with each other node_ccs = {}
    for i in g.nodes.keys():
        mutual_neighbor_count = 0
        neighbor_list = g.neighbors(i) 
        neighbor_set = {}
        for j in neighbor_list:
            neighbor_set[j] = 1 
        for j in neighbor_list:
            # We grab the neighbors and find out how many of them are in the # set
            new_neighbor_list = g.neighbors[j]
            for k in new_neighbor_list:
                if k != i and neighbor_list.has_key(k): 
                    mutual_neighbor_count += 1
        # We now calculate the coefficient by dividing by d*(d-1) to get the # fraction
        cc = float(mutual_neighbor_count)/((float(len(neighbor_list) * (len(neighbor_list) -1 ))))
        node_ccs[i] = cc
    total_cc = reduce(lambda a,b:node_ccs[a] + node_ccs[b], node_ccs.keys()) 
    total_cc = total_cc/len(g.nodes.keys())
    return total_cc
