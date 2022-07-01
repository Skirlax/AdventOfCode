from copy import deepcopy
import numpy as np




def load_matrix():
    with open("cucu_map.txt", "r") as file:
        matrix = np.array([list(line.strip()) for line in file.readlines()])
        return matrix


def simulation():
    matrix = load_matrix()
    cucumbers_to_replace = 0
    move = 0
    while True:
        matrix_copy = deepcopy(matrix)
        
        matrix, cucumbers_to_replace = check_east(matrix)
        matrix = replace_cucumbers(cucumbers_to_replace, "east", matrix)

        matrix, cucumbers_to_replace = check_south(matrix)
        matrix = replace_cucumbers(cucumbers_to_replace, "south", matrix)
        
        
        
        move += 1
        if np.array_equal(matrix_copy, matrix):
            break
        
        
    print(f"Cucumbers stopped moving after move {move}.")
    with open("result.txt", "w+") as file:
            for x in matrix:
                file.write(str(x) + '\n')


def check_east(matrix):
    cucumbers_to_replace = []
    for row_index,row in enumerate(matrix):
        for index, cucumber in enumerate(row):
            if cucumber == ">":
                if index + 1 == len(row):
                    if matrix[row_index][0] == ".":
                        cucumbers_to_replace.append([[row_index, index],[row_index, 0]])

                    break
            
               
                if matrix[row_index][index + 1] == ".":
                    cucumbers_to_replace.append([[row_index, index], [row_index, index + 1]])

             
            
               

    return matrix, cucumbers_to_replace

def check_south(matrix):
    cucumbers_to_replace = []
    for row_index,row in enumerate(matrix):
        
        for index, cucumber in enumerate(row):
            
    
                    
            if cucumber == "v":
                if row_index + 1 == len(matrix):
                    if matrix[0][index] == ".":
                        cucumbers_to_replace.append([[row_index, index],[0, index]])
                        
                    continue
                    
            
                    
                if matrix[row_index + 1][index] == ".":
                    cucumbers_to_replace.append([[row_index, index], [row_index + 1, index]])
            
         


    return matrix, cucumbers_to_replace


def replace_cucumbers(cucumbers_to_replace, direction, matrix):
    if cucumbers_to_replace is None:
        return matrix
    
    if direction == "east":
        for x in cucumbers_to_replace:
            matrix[x[0][0]][x[0][1]] = "."
            matrix[x[1][0]][x[1][1]] = ">"

    elif direction == "south":
        for x in cucumbers_to_replace:
           
        
            matrix[x[0][0]][x[0][1]] = "."
            matrix[x[1][0]][x[1][1]] = "v"

    return matrix
            
            



if __name__ == "__main__":
    simulation()