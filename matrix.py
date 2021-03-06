"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for a in range(4):
        line = ""
        for b in range(len(matrix)):
            line += str(matrix[b][a]) + "  "
        print(line)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            matrix[b][a] = 0
            if a==b:
                matrix[b][a] = 1 



#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for x in range(len(m2)):
        temp = []
        for i in range(4):
            temp.append(m2[x][i])
        for a in range(4):
            total = 0
            for c in range(4):
                total += temp[c] * m1[c][a]
            m2[x][a] = total




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m






















