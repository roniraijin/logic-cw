def unit_propagate(clause_set):
    answer = set()  
    max_var = max(abs(lit) for clause in clause_set for lit in clause)  

    def is_satisfied(clause_set):
        for clause in clause_set:
            if not any(lit in answer for lit in clause):  
                return False
        return True
    def propagate(clause):
        for i in clause:
            if len(i) > 1:
                return
            else:
                answer.append(i[0])
                clause.remove(i)
                propagate(clause)
                


        
        
        ...

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
    
    
    
    
    


clause_set = [[1],[-1,2]]
print(unit_propagate(clause_set))
