class Graph:
    def __init__(self, V: list, E: dict):
        self.V = V
        self.E = E


# warshall
def warshall(linked: list) -> list:
    n = len(linked)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                linked[i][j] = linked[i][j] or linked[i][k] and linked[k][j]
    return linked


# floyd
def floyd(linked: list) -> list:
    n = len(linked)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                linked[i][j] = min(linked[i][j], linked[i][k] + linked[k][j])
    return linked


# prim
# def prim(g: Graph) -> dict:
#     vt = [g.V[0]]
#     et = []
#     for i in vt:
#         for j in g.V:
#             m = None
#             if j not in vt:
#                 if i+j in g.E.keys():
#                     m = min(g.E[i+j], m) if m else g.E[i+j]
#         if m:
#             vt.append(m[1])
#             et.append(m)
#     return et
#
# # Dijkstra
# def Dijkstra(g: Graph) ->:



