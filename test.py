def unit_propagate(clause_set):
    answer = set()
    
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
                propagate(reduced_clauses)


    
    def propagate(clauses):
        if all(item == [] for item in clauses):
            return []
        for i in clauses:
            if len(i) != 1:
                pass
            if len(i) == 1:
                #print(i)
                answer.add(i[0])
                iteration(clauses, i[0])
        
    propagate(clause_set)    
    return answer

    
    


sat1 = [[1],[-1,2]]
print(unit_propagate(sat1))