# Classe para representar uma aresta entre dois vértices do grafo
class Edge:
    # Aresta que liga os pontos u e v com peso w

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, e):  # Operador será usado pela função sort
        return self.w < e.w


# Implementação do DSU, reusado da aula de DSU

MAXN = 1000010

parent = [0] * MAXN
size = [0] * MAXN


def find(value):
    if parent[value] == value:
        return value
    parent[value] = find(parent[value])
    return parent[value]


def merge(i, j):
    i = find(i)
    j = find(j)

    if i == j:
        return

    if size[i] >= size[j]:
        parent[j] = i
        size[i] += size[j]
    else:
        parent[i] = j
        size[j] += size[i]


def init_dsu(n):  # Initializa o DSU com n vértices
    for i in range(n):
        size[i] = 1
        parent[i] = i


class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        # Trocado de lista de adjacência para lista de arestas
        self.edges = []

    def add_edge(self, u, v, w):
        edge = Edge(u, v, w)  # Cria uma nova aresta
        self.edges.append(edge)  # Adiciona a nova aresta a nossa lista de arestas

    # Algoritmo de Kruskal
    def kruskal(self):
        self.edges.sort()  # Ordena as arestas por seu peso
        init_dsu(self.n)

        mst_cost = 0

        for i in range(len(self.edges)):  # Itera pela arestas
            u = self.edges[i].u
            v = self.edges[i].v

            if find(u) != find(v):  # Checa se u e v estão em componentes diferentes
                merge(u, v)
                mst_cost += self.edges[i].w  # Aumenta o custo da nossa MST

        return mst_cost


n, m = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

mst_cost = graph.kruskal();

print(f"MST tem custo {mst_cost}")

