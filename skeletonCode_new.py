
def load_dimacs(file_name):
    #file_name will be of the form "problem_name.txt"
    with open('file_name.txt', 'r') as d:
        d = d.readlines()
    d.pop(0)
    clause_set = {}
    for x in d:
        temp = {}  
        for t in x.split():
            if t != '0':
                try:    
                    temp.append(int(t))  
                except ValueError:
                    pass
        if temp:  
            clause_set.append(temp)

    print(clause_set)


def simple_sat_solve(clause_set):
    def simple_sat_solve(clause_set):
    answer = set()  # Track variable assignments
    max_var = max(abs(lit) for clause in clause_set for lit in clause)  # Find the highest variable

    def is_satisfied(clause_set):
        """Check if all clauses have at least one True literal"""
        for clause in clause_set:
            if not any(lit in answer for lit in clause):  # If no literal is satisfied
                return False
        return True

    def start(variable):
        if variable > max_var:  # Base case: All variables assigned
            if is_satisfied(clause_set):  # Check if formula is satisfied
                print("Solution found:", list(answer))
                return list(answer)
            return None  # If no valid assignment found

        for val in [variable, -variable]:  # Try both True and False assignments
            answer.add(val)  # Assign the variable
            result = start(variable + 1)  # Recur for the next variable
            if result is not None:  # If a solution was found, return it
                return result
            answer.remove(val)  # Backtrack if it doesn't work

        return None  # If no assignment works

    return start(1)  # Start with variable 1

# Test
sat1 = [[1], [1, -1], [-1, -2]]
solution = simple_sat_solve(sat1)
print("Final Solution:", solution)


def branching_sat_solve(clause_set,partial_assignment):
    ...


def unit_propagate(clause_set):
    ...


def dpll_sat_solve(clause_set,partial_assignment):
    ...



def test():
    print("Testing load_dimacs")
    try:
        dimacs = load_dimacs("sat.txt")
        assert dimacs == [[1],[1,-1],[-1,-2]]
        print("Test passed")
    except:
        print("Failed to correctly load DIMACS file")

    print("Testing simple_sat_solve")
    try:
        sat1 = [[1],[1,-1],[-1,-2]]
        check = simple_sat_solve(sat1)
        assert check == [1,-2] or check == [-2,1]
        print("Test (SAT) passed")
    except:
        print("simple_sat_solve did not work correctly a sat instance")

    try:
        unsat1 = [[1, -2], [-1, 2], [-1, -2], [1, 2]]
        check = simple_sat_solve(unsat1)
        assert (not check)
        print("Test (UNSAT) passed")
    except:
        print("simple_sat_solve did not work correctly an unsat instance")

    print("Testing branching_sat_solve")
    try:
        sat1 = [[1],[1,-1],[-1,-2]]
        check = branching_sat_solve(sat1,[])
        assert check == [1,-2] or check == [-2,1]
        print("Test (SAT) passed")
    except:
        print("branching_sat_solve did not work correctly a sat instance")

    try:
        unsat1 = [[1, -2], [-1, 2], [-1, -2], [1, 2]]
        check = branching_sat_solve(unsat1,[])
        assert (not check)
        print("Test (UNSAT) passed")
    except:
        print("branching_sat_solve did not work correctly an unsat instance")


    print("Testing unit_propagate")
    try:
        clause_set = [[1],[-1,2]]
        check = unit_propagate(clause_set)
        assert check == []
        print("Test passed")
    except:
        print("unit_propagate did not work correctly")


    print("Testing DPLL") #Note, this requires load_dimacs to work correctly
    problem_names = ["sat.txt","unsat.txt"]
    for problem in problem_names:
        try:
            clause_set = load_dimacs(problem)
            check = dpll_sat_solve(clause_set,[])
            if problem == problem_names[1]:
                assert (not check)
                print("Test (UNSAT) passed")
            else:
                assert check == [1,-2] or check == [-2,1]
                print("Test (SAT) passed")
        except:
            print("Failed problem " + str(problem))
    print("Finished tests")
