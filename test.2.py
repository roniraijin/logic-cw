def branching_sat_solve(clause_set,partial_assignment):
    

    def iterate(clause_set, partial_assignment):
        for i in partial_assignment:
            for clause in clause_set:
                if i in clause:
                    clause.remove(i)
        return partial_assignment
    literals = set()
    for clause in clause_set:
        for literal in clause:
            if literal not in literals:
                literals.add(abs(literal))
    for literal in literals:
        for i in [True,False]:
            clause_set_copy = clause_set.copy()
            partial_assignment_copy = partial_assignment.copy()
            if i:    
                partial_assignment_copy.append(literal)
            else:
                partial_assignment_copy.append(-literal)
            iterate(clause_set_copy, partial_assignment)




        ...






branching_sat_solve([[1],[2],[4],[-3,5]], [])
