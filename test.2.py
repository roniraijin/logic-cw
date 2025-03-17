def load_dimacs(file_name):
    #file_name will be of the form "problem_name.txt"
    with open(f'{file_name}', 'r') as d:
        d = d.readlines()
    print(d)
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
    return(clause_set)


def test():
    print("Testing load_dimacs")
    try:
        dimacs = load_dimacs("sat.txt")
        assert dimacs == [[1],[1,-1],[-1,-2]]
        print("Test passed")
    except:
        print("Failed to correctly load DIMACS file")
test()