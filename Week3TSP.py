from sys import maxsize
from itertools import permutations
def travellingSalesmanProblem(graph,s):
    v=len(graph)
    if v==1:
        return 0
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
        min_path=min(min_path,current_pathweight)
    return min_path

#Test Case-1
print("Test Case-1: Small Complete Graph")
graph1=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
    ]
print("Minimum Tour Cost: ",travellingSalesmanProblem(graph1,0))
print()

#Test case-2
print("Test Case-2: Triangle Graph")
graph2=[
    [0,5,10],
    [5,0,8],
    [10,8,0]
    ]
print("Minimum Tour Cost: ",travellingSalesmanProblem(graph2,0))
print()

#Test Case-3
print("Test Case-3: Bipartite Graph")
graph3=[
    [0,4,6,8],
    [4,0,5,7],
    [6,5,0,3],
    [8,7,3,0]
    ]
print("Minimum Tour Cost: ",travellingSalesmanProblem(graph3,0))
print()

#Test Case-4
print("Test Case-4: One-City TSP")
graph4=[
    [0]
    ]
print("Minimum Tour Cost: ",travellingSalesmanProblem(graph4,0))
