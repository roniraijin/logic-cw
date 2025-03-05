def load_dimacs(file_name):
    #file_name will be of the form "problem_name.txt"
    with open(file_name, 'r') as d:
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

    print(clause_set)


load_dimacs('sat.txt')