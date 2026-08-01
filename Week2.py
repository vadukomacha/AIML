def a_star(graph,h,start,goal):
    open_list=[start]
    closed_list=[]
    g={start:0}
    parent={start:None}
    while open_list:
        current=min(open_list,key=lambda x:g[x]+h[x])
        if current==goal:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            path.reverse()
            print("Path: ",path)
            print("Total Cost: ",g[goal])
            return
        for child,cost in graph[current]:
            new_cost=g[current]+cost
            if child not in open_list and child not in closed_list:
                open_list.append(child)
                parent[child]=current
                g[child]=new_cost
            elif child in open_list and new_cost<g[child]:
                g[child]=new_cost
                parent[child]=current
        open_list.remove(current)
        closed_list.append(current)
    print("Failure: Path not Found")
    
#Test Case-1
graph1={
    'S':[('A',1),('G',10)],
    'A':[('B',2),('C',1)],
    'B':[('D',5)],
    'C':[('D',3),('G',4)],
    'D':[('G',2)]
    }
h1={
    'S':5,
    'A':3,
    'B':4,
    'C':2,
    'D':1,
    'G':0
    }
print("Test Case 1: Graph with Admissible Heuristic")
a_star(graph1,h1,'S','G')
print()

#Test Case-2
graph2={
    'S':[('A',2),('B',4)],
    'A':[('G',5)],
    'B':[('G',2)],
    'G':[]
    }
h2={
    'S':3,
    'A':2,
    'B':1,
    'G':0
    }
print("Test Case 2: Multiple Possible Paths")
a_star(graph2,h2,'S','G')
print()

#Test Case-3
graph3={
    'S':[('G',3)],
    'G':[]
    }
h3={
    'S':1,
    'G':0
    }
print("Test Case 3: Direct Start-Goal Connection")
a_star(graph3,h3,'S','G')
print()

#Test Case-4
graph4={
    'S':[('A',1)],
    'A':[('B',2)],
    'B':[],
    'G':[]
    }
h4={
    'S':3,
    'A':2,
    'B':1,
    'G':0
    }
print("Test Case 4: Goal Not Reachable")
a_star(graph4,h4,'S','G')
print()

#Test Case-5
graph5={
    'S':[('A',1),('B',2)],
    'A':[('G',10)],
    'B':[('G',2)],
    'G':[]
    }
h5={
    'S':1,
    'A':0,
    'B':100,
    'G':0
    }
print("Test Case 5: Misleading Heursitic")
a_star(graph5,h5,'S','G')


