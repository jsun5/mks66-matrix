from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

w = 4
h = 4
IDENT = [[0 for x in range(w)] for y in range(h)]
ident(IDENT)

#Assignment:

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

matrix_mult(A,B)
print_matrix(A)
print_matrix(B)

matrix_mult(B,A)
print_matrix(A)
print_matrix(B)

matrix_mult(IDENT,A)
print_matrix(A)