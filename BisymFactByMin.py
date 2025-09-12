import numpy
import csv
from datetime import datetime


def integer_matrix_check(B): #Check if a matrix B is (approximately) an integer matrix
  check = True
  for i in range(0,2):
    for j in range(0,2):
      #Check if any matrix entries are non-integer
      decimal = B[i,j]%1
      if decimal>.0001 and decimal<.9999:
        check = False
      #Check if any matrix values are negative
      if B[i,j]<0.0001:
        check = False
  return check

def bisym_check(matrix): #Check if an integer matrix is bisymmetric and return True or False
  check = False
  #Check if both diagonal entries are equal
  if matrix[0,0]==matrix[1,1] and matrix[1,0]==matrix[0,1]:
    check = True
  return check


m= 4 #minimum value of x - At least 4
M =80 #maximum value of x



with open("BisymData"+str(m)+"to"+str(M)+".csv", 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['x','y','a','b','c','d','e','f','g','h', 'Bisymmetric factors'])
    for x in range(m,M+1):
        for y in range(x+1,2*(x-1)*(x-1)+1):
            detX= x*x-y*y
            if numpy.gcd(x,y)==1:#Comment out to get all matrices, including when gcd(x,y)!=1
                for a in range(1,x-1):
                  for b in range(1,x-a):
                    if numpy.gcd(a,b)==1: #Exclude top row shared factor
                      for c in range(1,x-1):
                        for d in range(1,x-c):
                          if numpy.gcd(c,d)==1: #Exclude bottom row shared factor
                            if a*d-b*c !=0 and numpy.sign(a-c) != numpy.sign(b-d): #Checks that A is doubly balanced and detA is nonzero
                                if detX%(a*d-b*c)==0: #Check if detA divides detX
                                  X=numpy.array([[x,y],[y,x]])
                                  A = numpy.array([[a,b],[c,d]])
                                  Ainverse = numpy.linalg.inv(A)
                                  B = numpy.dot(Ainverse, X)
                                  if integer_matrix_check(B)==True: #determines if factorization is into non-negative integer matrices
                                    e=round(B[0,0])
                                    f=round(B[0,1])
                                    g=round(B[1,0])
                                    h=round(B[1,1])
                                    if bisym_check(A)==True:
                                        bisym_factor=True
                                    else:
                                        bisym_factor=False
                                        print("Factorization is not bisymmetric")
                                    writer.writerow([x,y,a,b,c,d,e,f,g,h, bisym_factor])
        print("Minimum value: ",x) #Print maximum when all possible factors are checked
        print(datetime.now())
        

