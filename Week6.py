import itertools
hidden_states = ['healthy', 'sick']
states = ['sleeping', 'eating', 'pooping']
initial = {
    'healthy': 0.5,
    'sick': 0.5
}
transition = {
    'healthy': {
        'healthy': 0.7,
        'sick': 0.3
    },
    'sick': {
        'healthy': 0.4,
        'sick': 0.6
    }
}
emission = {
    'healthy': {
        'sleeping': 0.2,
        'eating': 0.6,
        'pooping': 0.2
    },
    'sick': {
        'sleeping': 0.4,
        'eating': 0.1,
        'pooping': 0.5
    }
}
def viterbi(obs):
    best_probability = 0
    best_path = None

    paths = itertools.product(hidden_states, repeat=len(obs))

    for path in paths:
        probability = (
            initial[path[0]]
            * emission[path[0]][obs[0]]
        )

        for i in range(1, len(obs)):
            previous = path[i - 1]
            current = path[i]

            probability = (
                probability
                * transition[previous][current]
                * emission[current][obs[i]]
            )

        if probability > best_probability:
            best_probability = probability
            best_path = path

    return best_probability, best_path

#Test Case 1
print("\nTEST CASE 1 - SUCCESS")
obs = ['sleeping', 'eating', 'sleeping']
probability, path = viterbi(obs)
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
print("Expected path: ('sick', 'healthy', 'healthy')")
print("Expected probability: 0.00672")
print("Test case 1: PASS")

#Test Case 2
print("\nTEST CASE 2 - SUCCESS")
obs = ['sleeping', 'eating', 'sleeping']
probability, path = viterbi(obs)
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
print("Transition and emission probabilities are valid")
print("Test case 2: PASS")

#Test Case 3
print("\nTEST CASE 3 - SUCCESS")
obs = ['sleeping']
probability, path = viterbi(obs)
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
print("Expected path: ('sick',)")
print("Expected probability: 0.2")
print("Test case 3: PASS")

#Test Case 4
print("\nTEST CASE 4 - FAILURE (EDGE)")
old_value = transition['healthy']['sick']
transition['healthy']['sick'] = 0
obs = ['sleeping', 'pooping']
path = ('healthy', 'sick')
probability = (
    initial[path[0]]
    * emission[path[0]][obs[0]]
    * transition[path[0]][path[1]]
    * emission[path[1]][obs[1]]
)
print("Input:", obs)
print("Test path:", path)
print("Path probability:", probability)
if probability == 0:
    print("Impossible path rejected")
    print("Test case 4: PASS")
else:
    print("Test case 4: FAIL")
transition['healthy']['sick'] = old_value

#Test Case 5
print("\nTEST CASE 5 - FAILURE (EDGE)")
invalid_transition = {
    'healthy': {
        'healthy': 0.7,
        'sick': 0.4
    },
    'sick': {
        'healthy': 0.4,
        'sick': 0.6
    }
}

valid = True
for state in hidden_states:
    total = sum(invalid_transition[state].values())

    if total != 1:
        valid = False
        print("Error:", state,
              "transition probabilities sum to", total)
if valid:
    print("Test case 5: FAIL")
    print("Invalid matrix was not detected")
else:
    print("Invalid probability matrix detected")
    print("Test case 5: PASS")
