def branching_sat_solve(clause_set,partial_assignment):
    ...
    literals = set()
    for clause in clause_set:
        for literal in clause:
            if literal not in literals:
                literals.add(abs(literal))
    print(literals)




branching_sat_solve([[1],[2],[4],[-3,5]], [])