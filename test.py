def unit_propagate(clause_set):
    answer = set()
    
    def iteration(clause, assignment):
        global reduced_clauses
        reduced_clauses = [clause for clause in clause_set if assignment not in clause]
        print(reduced_clauses)
        for clause in reduced_clauses:
            if -assignment in clause:
                clause.remove(-assignment)
                propagate(reduced_clauses)


    
    def propagate(clause):
        for i in clause:
            if len(i) != 1:
                pass
            else:
                answer.add(i[0])
                iteration(clause_set, i[0])
        return(reduced_clauses)

    propagate(clause_set)
    

    
    


clause_set = [[1],[-1,2]]
print(unit_propagate(clause_set))
