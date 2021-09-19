#implementing BFS, DFS
import collections

def bfs(visited,graph,root):
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        for i in graph[vertex]:
            if (i not in queue) and (i not in visited):
                queue.append(i)

def dfs(visited,graph,root):
    if root not in visited:
        visited.append(root)
        for v in graph[root]:
            dfs(visited,graph,v)

if __name__ == "__main__":
    graph = {}
    bfsVisited = []
    dfsVisited = []

    vertex = int(input("Enter Total Vertex Number: "))
    for i in range(vertex):
        graph[i] = []
        neighbor = int(input("Enter Total Neighbor Number of "+str(i)+": "))
        for j in range(neighbor):
            v = int(input("Enter "+str(j+1)+"th Neighbor of "+str(i)+": "))
            graph[i].append(v)

    bfs(bfsVisited,graph,0)
    dfs(dfsVisited,graph,0)

    print("Graph = ",graph)
    print("BFS = ",bfsVisited)
    print("DFS = ",dfsVisited)