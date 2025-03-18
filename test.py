import itertools as iter
import time

def branching_sat_solve(clause_set, partial_assignment=[]):
    """Brute-force SAT solver using itertools that respects partial_assignment."""
    start_time = time.time()  # Start timing

    def is_satisfied(assignment):
        """Check if the clause set is satisfied under the given assignment."""
        for clause in clause_set:
            if not any(assignment.get(abs(lit), False) == (lit > 0) for lit in clause):
                return False  # Clause is not satisfied
        return True

    # Extract all variables
    all_vars = {abs(lit) for clause in clause_set for lit in clause}
    
    # Convert partial_assignment to a dictionary
    assignment_dict = {abs(lit): lit > 0 for lit in partial_assignment}
    
    # Find unassigned variables
    unassigned_vars = list(all_vars - set(assignment_dict.keys()))

    # Generate all possible truth assignments for the remaining variables
    for remaining_assignment in iter.product([True, False], repeat=len(unassigned_vars)):
        # Merge partial_assignment with new variable assignments
        full_assignment = assignment_dict.copy()
        full_assignment.update(dict(zip(unassigned_vars, remaining_assignment)))

        if is_satisfied(full_assignment):
            elapsed_time = time.time() - start_time
            print(f"Solved in {elapsed_time:.6f} seconds")
            return [lit if full_assignment[lit] else -lit for lit in all_vars]  # Return assignment as literals
    
    elapsed_time = time.time() - start_time
    print(f"No solution found. Time taken: {elapsed_time:.6f} seconds")
    return False  # No satisfying assignment found

# Example usage:
clauses = [
    [1, -2, 3], [-1, 4, -5], [2, -3, 6], [1, -4, 5], 
    [-6, 2, 3], [3, 4, -1], [-2, -4, 6], [-3, 5, -6],
    [1, 2, -5], [-1, 3, 4], [2, -6, 5], [-4, 6, -1], 
    [3, -5, 2], [-6, 4, 1], [1, -2, -3, 4, -5, 6]
]  

partial_assignment = [1, -3]  # Example partial assignment

print(branching_sat_solve(clauses, partial_assignment))
