def unit_propagate(clause_set):
    answer = set()
    x = clause_set.copy()
    def iteration(clauses, assignment):
        reduced_clauses = clauses.copy()
        reduced_clauses = [clause for clause in clauses if assignment not in clause]
        print(f"Reduced clauses after assignment {assignment}: {reduced_clauses}")

        if reduced_clauses == []:
            return []
        for clause in reduced_clauses:
            if -assignment in clause:
                
                clause.remove(-assignment)
                print(f"Clause after removal of {-assignment}: {clause}")
        return propagate(reduced_clauses)


    
    def propagate(clauses):
        if all(item == [] for item in clauses):
            return []
        if clauses == []:
            return []
        for i in clauses:
            if len(i) != 1:
                pass
            if len(i) == 1:
                answer.add(i[0])
                clausecopy = clauses.copy()
                iteration(clausecopy, i[0])
                print(f'{clauses} is idk')
                return clauses        
        
    return propagate(x)    
    

    
    


sat1 = [[1],[-1,2]]
if unit_propagate(sat1) == []:
    print(unit_propagate(sat1))
    print('True')
else:
    print(unit_propagate(sat1))
    print("False")