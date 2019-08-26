from Vector import Vector

class Matrix(list):
    def __init__(self,A,j = None):
        if (A):
            if (A.__class__.__name__=='int'):
                if (not j):
                    j = A

                for i in range(A):
                    self.append(Vector([]))
                    self[i].__Calloc__(j)


            elif (A.__class__.__name__ in [ 'Matrix', 'list'] ):
                for i in range( len(A) ):
                    self.append(Vector([]))

                    for j in range( len(A[i]) ):
                        self[i].append( 1.0*A[i][j] )
            else:
                print "Matrix.init: Invalid first argument type",A,"'"+A.__class__.__name__+"'"
                exit()

    def __str__(A):
        text = []
        for i in range( len(A) ):
            text.append( A[i].__str__() )

        return "{\n   "+",\n   ".join(text)+"\n}"

    def __add__(A,B):
        if (len(A) != len(B)):
            print "Matrix.add: Incompatible dimensions",len(A),len(B)
            exit()

        #Matrix allocated with zeros (calloc)
        C = Matrix(len(A),len(A[0]))
        for i in range( len(A) ):
            if ( len(A[i]) != len(B[i]) ):
                print "Matrix.add, row",i,": Incompatible dimensions",len(A[i]),len(B[i])
                exit()
                
            for j in range(len(A[i])):
                C[i][j] = 1.0*(A[i][j] + B[i][j])

        return C

    def __mul__(A,B):
        if (B.__class__.__name__ in [ 'int','float' ]):
            #Scalar: Return Matrix,
            return A.__mul_Scalar__(B)
            
        if (B.__class__.__name__ in [ 'Vector' ]):
            #Vector: Return Vector,
            return A.__mul_Vector__(B)
        
        if (B.__class__.__name__ in [ 'Matrix' ]):
            #Matrix: Return Matrix
            return A.__mul_Matrix__(B)
        
        print "Matrix.mul: Invalid second argument type",B
        exit()

    def __mul_Scalar__(A,B):
        C = Matrix(len(A),len(A[0]))

        for i in range(len(C)):
            for j in range(len(C[0])):
                C[i] = A[i]*B

        return C

    def __mul_Vector__(A,B):
        if (len(A[0]) != len(B)):
            print "Matrix.mul: Incompatible dimensions",len(A[0]),len(B)
            exit()
        else:
            C = Vector(len(A))

            for i in range(len(C)):
                for n in range(len(B)):
                    C[i] += A[i][n]*B[n]

            return C       

    def __mul_Matrix__(A,B):
        if (len(A[0]) != len(B)):
            print "Matrix.mul: Incompatible dimensions",len(A[0]),len(B)
            exit()
        else:
            C = Matrix(len(A),len(B[0]))

        for i in range(len(C)):
            for j in range(len(C[0])):
                for n in range(len(A[0])):
                    C[i][j] += A[i][n]*B[n][j]

        return C

    def __rmul__(A,B):
        return A*B

    def __neg__(A):
        return A*(-1.0)

    def __sub__(A,B):
        return A+(-B)
            
    def __isub__(A,B):
        return A+(-B)

def Transpose(A): #Extra
    C = Matrix(len(A[0]), len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]

    return C

def Matrix_Zero(m,n):
    return Matrix(m,n)

def Matrix_Identity(n):
    I = Matrix(n)

    for i in range(n):
        I[i][i]=1.0

    return I

def Matrix_Diagonal(v):
    D = Matrix(len(v))

    for i in range(len(v)):
        D[i][i] = v[i]

    return D

def Matrix_Vandermonte(v):
    V = Matrix(len(v))

    for i in range( len(v) ):
        fact = 1.0
            
        for j in range( len(v) ):
            V[i][j] = fact
            fact *= v[i]

    return V

def Matrix_Dyadic(A,B):
    return A*Transpose(B)

def Matrix_Rotation(theta):
    return Matrix([ [cos(theta),-sin(theta)], [sin(theta),cos(theta)]])