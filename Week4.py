from sympy import symbols,Implies,Not,Xor
from sympy.logic.inference import satisfiable
Rain=symbols('Rain')
Harry_visited_Hagrid=symbols('Harry_visited_Hagrid')
Harry_visited_Dumbledore=symbols('Harry_visited_Dumbledore')
def run_test(test_name,kb):
    print("="*50)
    print(test_name)
    print(kb)
    if satisfiable(kb) is False:
        print("Knowledge Base is NOT satisfiable (Contradiction)")
        return
    print("Knowledge Base is satisfiable")
    rain_true=satisfiable(kb&Rain)
    rain_false=satisfiable(kb&Not(Rain))
    if rain_true and not rain_false:
        print("Conclusion: It rained today")
    elif rain_false and not rain_true:
        print("Conclusion: It did not rain today")
    else:
        print("Conclusion: Rain cannot be determined")

#Test Case 1
KB1=(
    Implies(Not(Rain),Harry_visited_Hagrid)
    & Xor(Harry_visited_Hagrid,Harry_visited_Dumbledore)
    & Harry_visited_Dumbledore
)
run_test("TEST CASE 1",KB1)

#Test Case 2
KB2=(
    Implies(Not(Rain),Harry_visited_Hagrid)
    & Xor(Harry_visited_Hagrid,Harry_visited_Dumbledore)
    & Harry_visited_Hagrid
    & Not(Rain)
)
run_test("TEST CASE 2",KB2)

#Test Case 3
KB3=(
    Implies(Not(Rain),Harry_visited_Hagrid)
    & Xor(Harry_visited_Hagrid,Harry_visited_Dumbledore)
    & Harry_visited_Dumbledore
    & Rain
)
run_test("TEST CASE 3",KB3)

#Test Case 4
KB4=(
    Implies(Not(Rain),Harry_visited_Hagrid)
    & Xor(Harry_visited_Hagrid,Harry_visited_Dumbledore)
    & Harry_visited_Hagrid
    & Harry_visited_Dumbledore
)
run_test("TEST CASE 4",KB4)

#Test Case 5
KB5=Implies(Not(Rain),Harry_visited_Hagrid)
run_test("TEST CASE 5",KB5)
