#implementing BFS, DFS
import collections

def bfs(explored,parent,graph,root,goal):
    queue = collections.deque([root])
    explored[root] = 1
    parent[root] = "none"
    is_end = False
    while queue:
        if is_end:
            break
        node = queue.popleft()
        explored[node] = 2
        for i in graph[node].keys():
            if(i==goal):
                is_end = True
                parent[i] = node
                break
            elif explored[i]==0:
                queue.append(i)
                explored[i] = 1
                parent[i] = node

if __name__ == "__main__":
    graph = {
    "Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
    }

    parent = {}
    explored = {}

    for i in graph.keys():
        explored[i] = 0

    root = "Arad"
    goal = "Bucharest"

    bfs(explored,parent,graph,root,goal)

    node = goal
    while parent[node] != "none":
        print(node)
        node = parent[node]
    print(node)