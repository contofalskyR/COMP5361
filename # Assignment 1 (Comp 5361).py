# Assignment 1 (Comp 5361)

# Question 1: Negation (-|)

def negation(value): 
    if value == "T":
        return "F"
    elif value == "F":
        return "T"
    else:
        return "Invalid Input"
    
print("Negation:")
print(f"Negation of T is {negation('T')}")
print(f"Negation of F is {negation('F')}\n")

# Question 2: Conjunction (^)

def conjunction(value1, value2):
    if value1 == "T" and value2 == "T":
        return "T"
    elif value1 == "F" or value2 == "F":
        return "F"
    else:
        return "Invalid Input"
    
print("Conjunction:")
print(f"T ^ T = {conjunction('T', 'T')}")
print(f"T ^ F = {conjunction('T', 'F')}")
print(f"F ^ T = {conjunction('F', 'T')}")
print(f"F ^ F = {conjunction('F', 'F')}\n")

# Question 3: Disjunction (V) 

def disjunction(value1, value2):
    if value1 == "T" or value2 == "T":
        return "T"
    if value1 == "F" and value2 =="F":
        return "F"
    else: 
        return "Invalid Input"
    
print("Disjunction:")
print(f"T v T = {disjunction('T', 'T')}")
print(f"T v F = {disjunction('T', 'F')}")
print(f"F v T = {disjunction('F', 'T')}")
print(f"F v F = {disjunction('F', 'F')}\n")

# Question 4: Implication (-->)

def implication(value1, value2):
    if value1 == "T" and value2 == "T":
        return "T"
    elif value1 == "T" and value2 == "F":
        return "F"
    elif value1 == "F" and value2 == "F":
        return "T"
    elif value1 == "F" and value2 == "T":
        return "T"
    
print("Implication:")
print(f"T --> T = {implication('T', 'T')}")
print(f"T --> F = {implication('T', 'F')}")
print(f"F --> T = {implication('F', 'T')}")
print(f"F --> F = {implication('F', 'F')}\n")

# Question 5: Biconditional (<-->)

def biconditional(value1, value2):
    if value1 == "T" and value2 == "T" or value1 == "F" and value2 == "F":
        return "T"
    elif value1 == "T" and value2 == "F" or value1 == "F" and value2 =="T":
        return "F"
    else:
        return "Invalid Input"
    
print("Biconditional:")
print(f"T <--> T = {biconditional('T', 'T')}")
print(f"T <--> F = {biconditional('T', 'F')}")
print(f"F <--> T = {biconditional('F', 'T')}")
print(f"F <--> F = {biconditional('F', 'F')}\n")