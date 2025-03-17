
def load_dimacs(file_name):
    #file_name will be of the form "problem_name.txt"
    with open(f'{file_name}', 'r') as d:
        d = d.readlines()
    d.pop(0)
    clause_set = []
    for x in d:
        temp = []  
        for t in x.split():
            if t != '0':
                try:    
                    temp.append(int(t))  
                except ValueError:
                    pass
        if temp:  
            clause_set.append(temp)

    return(clause_set)


def simple_sat_solve(clause_set):
    answer = set()  
    max_var = max(abs(lit) for clause in clause_set for lit in clause)  

    def is_satisfied(clause_set):
        
        for clause in clause_set:
            if not any(lit in answer for lit in clause):  
                return False
        return True

    def start(variable):
        if variable > max_var: 
            if is_satisfied(clause_set):  
                return list(answer)
            return None  

        for val in [variable, -variable]:  
            answer.add(val) 
            result = start(variable + 1) 
            if result is not None:  
                return result
            answer.remove(val)  

        return None 

    return start(1)  








def branching_sat_solve(clause_set,partial_assignment):
    reduced_clauses = []
    for clause in clause_set:
        if any(lit in partial_assignment for lit in clause):  
            continue  
        reduced_clause = [lit for lit in clause if -lit not in partial_assignment]
        if not reduced_clause:  
            return False
        reduced_clauses.append(reduced_clause)

    
    if not reduced_clauses:
        return partial_assignment  

    
    for clause in reduced_clauses:
        for lit in clause:
            if lit not in partial_assignment and -lit not in partial_assignment:
                variable = abs(lit)
                break
        else:
            continue
        break

    
    result = simple_sat_solve(reduced_clauses, partial_assignment + [variable])
    if result:
        return result  

 
    return simple_sat_solve(reduced_clauses, partial_assignment + [-variable])




def unit_propagate(clause_set):
    
    
    def propagate(unit, p_set):    
        new_set = [clause for clause in p_set if unit not in clause]
        print(new_set)
        for clause in new_set:
            if -unit in clause:
                clause.remove(-unit)
        return new_set
    
    
    def iteration(Fortnite):
        clause_unit = None
        for clause in Fortnite:
            if len(clause) == 1:
                clause_unit = clause[0]
                sigma = propagate(clause_unit, Fortnite)
                if not sigma:
                    return []
                else:
                    return iteration(sigma)

        #print(clause_set)
        return Fortnite
    
    #print(iteration(clause_set))
    return(iteration(clause_set))



def dpll_sat_solve(clause_set,partial_assignment):
    ...
    def propagate(unit, p_set):    
        new_set = [clause for clause in p_set if unit not in clause]
        print(new_set)
        for clause in new_set:
            if -unit in clause:
                clause.remove(-unit)
        return new_set
    
    
    def iteration(Fortnite):
        clause_unit = None
        for clause in Fortnite:
            if len(clause) == 1:
                clause_unit = clause[0]
                sigma = propagate(clause_unit, Fortnite)
                if not sigma:
                    return []
                else:
                    return iteration(sigma)

        #print(clause_set)
        return Fortnite
    
    #print(iteration(clause_set))
    return(iteration(clause_set))
    
    reduced_clauses = []
    for clause in clause_set:
        if any(lit in partial_assignment for lit in clause):  
            continue  
        reduced_clause = [lit for lit in clause if -lit not in partial_assignment]
        if not reduced_clause:  
            return False
        reduced_clauses.append(reduced_clause)

    
    if not reduced_clauses:
        return partial_assignment  

    
    for clause in reduced_clauses:
        for lit in clause:
            if lit not in partial_assignment and -lit not in partial_assignment:
                variable = abs(lit)
                break
        else:
            continue
        break

    
    result = simple_sat_solve(reduced_clauses, partial_assignment + [variable])
    if result:
        return result  

 
    return simple_sat_solve(reduced_clauses, partial_assignment + [-variable])



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

test()