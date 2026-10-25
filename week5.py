P_Burglary = 0.002
P_Earthquake = 0.001

CPT_Alarm = {
    (True, True): 0.94,
    (True, False): 0.95,
    (False, True): 0.31,
    (False, False): 0.001
}

CPT_David = {
    (True, True): 0.91,
    (True, False): 0.09,
    (False, True): 0.05,
    (False, False): 0.95
}

CPT_Sophia = {
    (True, True): 0.75,
    (True, False): 0.25,
    (False, True): 0.02,
    (False, False): 0.98
}


def validate_probability(p):
    if not (0 <= p <= 1):
        raise ValueError("Probability must be between 0 and 1")


def joint_probability(B, E, A, D, S):

    validate_probability(P_Burglary)
    validate_probability(P_Earthquake)

    pB = P_Burglary if B else 1 - P_Burglary
    pE = P_Earthquake if E else 1 - P_Earthquake

    # Check Alarm CPT
    if (B, E) not in CPT_Alarm:
        return "Missing CPT value"

    pA = CPT_Alarm[(B, E)]

    if not A:
        pA = 1 - pA

    pD = CPT_David[(A, D)]
    pS = CPT_Sophia[(A, S)]

    return pB * pE * pA * pD * pS


# Test Case 1
result = joint_probability(False, False, True, True, True)
print("Test Case 1:", result)


# Test Case 2
result = joint_probability(True, False, True, True, True)
print("Test Case 2:", result)


# Test Case 3
result = joint_probability(False, True, True, True, False)
print("Test Case 3:", result)


# Test Case 4: Missing CPT value
CPT_Alarm.pop((False, False))

result = joint_probability(False, False, True, True, True)
print("Test Case 4:", result)


# Test Case 5: Invalid probability
try:
    validate_probability(-1.3)
    print("Test Case 5: Valid probability")
except ValueError as e:
    print("Test Case 5:", e)