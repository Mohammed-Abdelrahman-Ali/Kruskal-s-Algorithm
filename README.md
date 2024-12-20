# Kruskal-s-Algorithm

KRUSKAL(G):
    MST = {}  # Initialize an empty set for the Minimum Spanning Tree
    SORT edges of G by weight in non-decreasing order
    MAKE-SET(v) for each vertex v in G  # Initialize a disjoint-set for each vertex

   FOR each edge (u, v) in the sorted edges:
        IF FIND-SET(u) != FIND-SET(v):  # Check if u and v are in different sets
            ADD (u, v) to MST          # Include the edge in the MST
            UNION(u, v)                # Merge the sets containing u and v
    
   RETURN MST
