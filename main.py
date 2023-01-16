import time
from grid import Grid
from plot_results import PlotResults
import math

def select_variable_fa(grid):
    # domain: {1,....,9} ; variables: {X11, X12,......,X89, X99}
    # must return tuple (i,j) with the index on the grid whose domain is greater than 1
    # can use g.get_cells()[i][j] 
    
    #returning_tuple = ()
    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            domain_count = len(grid.get_cells()[i][j])
            if domain_count > 1:
                return (i, j) 
    

def select_variable_mrv(grid):
    # must return the tuple following MRV

    h_value = 81

    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            domain_count = len(grid.get_cells()[i][j])
            if domain_count > 1 and domain_count < h_value:
                h_value = domain_count  
                return (i, j) 
 

def search(grid, var_selector):
    if grid.is_solved():
        return grid, True
    
    var = var_selector
    
    domain_var = grid.get_cells()[var[0]][var[1]]
    for d in domain_var:
        if(is_consistent(grid, var, d) == True):
            copy_grid = grid.copy()
            copy_grid.get_cells()[var[0]][var[1]] = d
            rb, solution = search(copy_grid, select_variable_mrv(copy_grid))
            if solution != False:
                return rb, True
        
        #for j in range(grid.get_width()):
            
            # if grid.get_cell()[var[0]][j] == d:
            #     is_consistent = False
            # if grid.get_cell()[var[j]][1] == d:
            #     is_consistent = False
            
            # row_init = ( var[0]// 3) * 3
            # column_init = (var[1] // 3) * 3
            # for i in range(row_init, row_init + 3):
            #     for j in range(column_init, column_init + 3):
            #         if grid.get_cell()[var[i]][var[j]]
            #         is_consistent = False
        
    return None, False


def is_consistent(grid, var, d):
    # row
    for i in range(grid.get_width()):
        if grid.get_cells()[var[0]][i] == d:
            return False

    # col
    for i in range(grid.get_width()):
        if grid.get_cells()[i][var[1]] == d:
            return False
    
    #unit
    row_init = (var[0] // 3) * 3
    column_init = (var[1] // 3) * 3
    for i in range(row_init, row_init + 3):
                for j in range(column_init, column_init + 3):
                    if grid.get_cells()[i][j] == d:
                        return False
    
    return True 

# def col_consistency(grid, var, d):
#     for i in range(grid.get_width()):
#         if grid.get_cells()[i][var[1]] == d:
#             return False
    
#     return True 

# def unit_consistency(grid, var, d):
#     row_init = (var[0] // 3) * 3
#     column_init = (var[1] // 3) * 3
#     for i in range(row_init, row_init + 3):
#                 for j in range(column_init, column_init + 3):
#                     if grid.get_cells()[i][j] == d:
#                         return False
    
#     return True   
    
def forward_checking(grid, variable):
    
    r_row = grid.remove_domain_row(variable[0], variable[1])
    r_col = grid.remove_domain_column(variable[0], variable[1])
    r_unit = grid.remove_domain_unit(variable[0], variable[1])

    if r_row and r_col and r_unit:
        return True
    else: 
        return False


def pre_process_forward_checking(grid):
    
    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            return forward_checking(grid, (i, j))

    

file = open('tutorial_problem.txt', 'r')
problems = file.readlines()
for p in problems:
    g = Grid()
    g.read_file(p)

    
    a, b = search(g, select_variable_fa(g))
    a.print()
    print(b)
    # test your backtracking implementation without inference here
    # this test instance is only meant to help you debug your backtracking code
    # once you have implemented forward checking, it is fine to find a solution to this instance with inference

file = open('top95.txt', 'r')
problems = file.readlines()

for p in problems:
    g = Grid()
    g.read_file(p)
    
    # test your backtracking implementation with inference here