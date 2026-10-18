colors=['Red','Blue','Green']
colors_of_states={}
def promising(state,color,neighbors):
    for neighbor in neighbors.get(state):
        color_of_neighbor=colors_of_states.get(neighbor)
        if color_of_neighbor==color:
            return False
    return True
def get_color_for_state(state,neighbors):
    for color in colors:
        if promising(state,color,neighbors):
            return color
    return None
def graph_coloring(states,neighbors):
    colors_of_states.clear()
    for state in states:
        color=get_color_for_state(state,neighbors)
        if color is None:
            print("Coloring not possible")
            return False
        colors_of_states[state]=color
    print("Valid Coloring")
    print(colors_of_states)
    return True

#Test Case-1
print("Test Case-1: Triangle Graph")
states1=['A','B','C']
neighbors1={
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B']
    }
graph_coloring(states1,neighbors1)
print()

#Test Case-2
print("Test Case-2: Bipartite Graph")
states2=['A','B','C','D']
neighbors2={
    'A':['C','D'],
    'B':['C','D'],
    'C':['A','B'],
    'D':['A','B']
    }
graph_coloring(states2,neighbors2)
print()

#Test Case-3
print("Test Case-3: Complete Graph K4 with 3 colors")
states3=['A','B','C','D']
neighbors3={
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['A','B','D'],
    'D':['A','B','C']
    }
graph_coloring(states3,neighbors3)
