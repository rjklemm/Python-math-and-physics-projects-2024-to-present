#Bob Klemm
#9/17/2024

#Magic Square of Squares Unsolved Problem

import math

#Part 1: Are there common sums that occur enough times to create values for a magic square of squares?

def magicways(common_sum, diagonal, row_column):
    square_list = [] 
    square_list_2 = [[1,0]]
    corner_count = 0 
    middle_count = 0
    side_count = 0
    sides = [] #value has 2 occurences
    corners = [] #value has 3 occurences
    middles = [] #value has 4 occurences
    square_sum_list = [] #list of squares being summed together for a common sum
    square_ways_list = [] #list of frequencies of squares used in common sums
    row_column_count = 0
    diagonal_count = 0
    diagonal = []
    row_column = []
    x = math.ceil(math.sqrt(common_sum))# maximum tested value
    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                sum = a**2+b**2+c**2
                if sum == common_sum:
                    square_sum_list.append([a**2, b**2, c**2])
                    square_list.append(a**2)
                    square_list.append(b**2)
                    square_list.append(c**2)
    square_list.sort()
    last_square = 1

    for new_square in square_list:
        if new_square != last_square:
            square_list_2.append([new_square, 1])#count occurrences of squares
        else: 
            square_list_2[-1][1] += 1
            if square_list_2[-1][1] == 2:
                side_count += 1
                sides.append(new_square)
            if square_list_2[-1][1] == 3:
                corner_count += 1
                corners.append(new_square)
            if square_list_2[-1][1] == 4:
                middle_count += 1
                middles.append(new_square)
        last_square = new_square

    for squares in square_sum_list:
        square_ways = []
        for square in squares:
            if square in middles:
                square_ways.append(4)
            elif square in corners:
                square_ways.append(3)
            elif square in sides:
                square_ways.append(2)
            else: 
                square_ways.append(1)
        square_ways_list.append(square_ways)
        square_way_score = square_ways[0] + square_ways[1] + square_ways[2] #need "score" of 8 for rows and columns and 10 along diagonals

        if square_way_score >= 10: #candidates for diagonals in magic square
            diagonal_count += 1
            diagonal.append(squares)
        elif square_way_score >= 8: #candidates for rows or columns in magic square
            row_column_count += 1
            row_column.append(squares)

    print(common_sum, diagonal_count, row_column_count)

    if diagonal_count >= 2 and row_column_count >= 8: #four corners of magic square needed, plus middle and sides
    #print("The common sum is " + str(common_sum))   
    #print(square_list_2)
    #print(square_sum_list)
    #print(square_ways_list)

    
        print("Possible diagonal values are: ")
        print(diagonal)
        print("Possible row-column values are: ")
        print(row_column)
    
        return [common_sum, diagonal, row_column]

    else:
        return [0, 0, 0]


values = []
for value in range(100,20000): #previous run-through min common sum was greater than 4000 (4541)
    [value, diagonal, row_column] = magicways(value, [], [])   
    if value != 0:
        values.append(value) #save any possible common sums to sort through

print("possible common sums to create a magic square:")
print(values)

#There are possible square sums that occur enough times that need to be checked further.


#Part 2: Filling in a magic square with said possible values

#Sorting through the diagonal and row-column values to find a set of 9 unique squares that work 

def arrange_magic_square(common_sum):
    common_sum, diagonal, row_column = magicways(common_sum, [], [])

    square_list = [diagonal, row_column]
    square_list_2 = []
    sides = []
    corners = []
    middles = []
    last_square = 0

    for new_square in square_list:
        if new_square != last_square:
            square_list_2.append([new_square, 1])#count occurrences of squares
        else: 
            square_list_2[-1][1] += 1
            if square_list_2[-1][1] == 2:
                sides.append(new_square)
            if square_list_2[-1][1] == 3:
                corners.append(new_square)
            if square_list_2[-1][1] == 4:
                middles.append(new_square)
        last_square = new_square

    if len(middles) + len(corners) + len(sides) > 8:
        print("possible values for magic square")
        print(middles, corners, sides) 
        #magicways(value, [], [])   

for value in values:
    arrange_magic_square(value)

