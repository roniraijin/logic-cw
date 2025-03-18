import time

def branching_sat_solve(clause_set, partial_assignment=[]):
    """Recursive branching SAT solver with execution time measurement."""
    start_time = time.time()  # Start timing

    def solve(clause_set, partial_assignment):
        # Check if the clause set is already satisfied
        if all(any(lit in partial_assignment for lit in clause) for clause in clause_set):
            return partial_assignment  # Return satisfying assignment
        
        # Check if any clause is unsatisfied (i.e., contains no true literals)
        if any(all(-lit in partial_assignment for lit in clause) for clause in clause_set):
            return False  # Unsatisfiable
        
        # Select the next unassigned variable
        all_vars = {abs(lit) for clause in clause_set for lit in clause}
        assigned_vars = {abs(lit) for lit in partial_assignment}
        unassigned_vars = all_vars - assigned_vars
        
        if not unassigned_vars:
            return False  # No more variables to assign, unsatisfiable

        var = next(iter(unassigned_vars))  # Pick an arbitrary unassigned variable
        
        # Try setting the variable to True
        result = solve(clause_set, partial_assignment + [var])
        if result:
            return result
        
        # If that fails, try setting the variable to False
        return solve(clause_set, partial_assignment + [-var])

    result = solve(clause_set, partial_assignment)
    elapsed_time = time.time() - start_time  # Compute elapsed time
    print(f"Solved in {elapsed_time:.6f} seconds")  

    return result

# Example usage:
clauses = [
    [1, -2, 3], [-1, 4, -5], [2, -3, 6], [1, -4, 5], 
    [-6, 2, 3], [3, 4, -1], [-2, -4, 6], [-3, 5, -6],
    [1, 2, -5], [-1, 3, 4], [2, -6, 5], [-4, 6, -1], 
    [3, -5, 2], [-6, 4, 1], [1, -2, -3, 4, -5, 6]
]
  # Example CNF formula
print(branching_sat_solve(clauses))  # Returns a satisfying assignment if one exists
