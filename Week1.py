from collections import deque
def bfs(graph,start):
    visited=set()
    queue= deque([start])
    visited.add(start)
    traversal=[]
    while queue:
        node=queue.popleft()
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
def dfs(graph,start):
    visited=set()
    traversal=[]
    def dfs_visit(node):
        visited.add(node)
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_visit(neighbor)
    dfs_visit(start)
    return traversal

#Test Case-1
graph1={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B'],
    'F':['C']
    }
print("Test Case 1: Connected Graph")
print("BFS: ",bfs(graph1,'A'))
print("DFS: ",dfs(graph1,'A'))
print()

#Test Case-2
graph2={
    'A':['B','C','D'],
    'B':['A','E','F'],
    'C':['A','G'],
    'D':['A','H'],
    'E':['B'],
    'F':['B'],
    'G':['C'],
    'H':['D']
    }
print("Test Case 2: Multibranch Graph")
print("BFS: ",bfs(graph2,'A'))
print("DFS: ",dfs(graph2,'A'))
print()

#Test Case-3
graph3={
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B']
    }
print("Test Case 3: Cyclic Graph")
print("BFS: ",bfs(graph3,'A'))
print("DFS: ",dfs(graph3,'A'))
print()

#Test Case-4
graph4={
    'A':[]
    }
print("Test Case 4: Single Node")
print("BFS: ",bfs(graph4,'A'))
print("DFS: ",dfs(graph4,'A'))
print()

#Test Case-5
graph5={
    'A':['B'],
    'B':['A'],
    'C':['D'],
    'D':['C']
    }
print("Test Case 5: Disconnected Graph")
print("BFS: ",bfs(graph5,'A'))
print("DFS: ",dfs(graph5,'A'))
