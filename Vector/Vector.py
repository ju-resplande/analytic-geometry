from math import *

class Vector(list):
    def __init__(v,w=[]):
        if (w.__class__.__name__=="int"):
            v.__Calloc__(w)
            
        else:
            v.__Calloc__( len(w) )
            for i in range( len(w) ):
                v[i] = 1.0*w[i]
        
    def __Calloc__(v,size):
        for i in range(size):
            v.append(0.0)
        
    def __add__(v,w):        
        #Binary add: u=v+w
        u = Vector(v)
        for i in range(len(v)):
            u[i] += w[i]
        return u

    def __iadd__(v,w):
        #Unary add: u+=v. Superflous?
        return v + w

    
    def __sub__(v,w):
        #Binary subtraction: u=v-w
        u = Vector(v)
        for i in range(len(v)):
            u[i] -= w[i]
        
        return u

    def __isub__(v,w):
        #Unary subtraction: u-=v.
        return v - w

    def __neg__(u):
        #Vector neg: opposed vector
        return u * (-1.0)
    
    
    def __mul__(v,arg2):
        
        if (arg2.__class__.__name__ == "Vector"):
            return v.__mul_Vector__(arg2)

        #Second argument should be e scalar from now on.
        
        #Make sure it is float
        if (arg2.__class__.__name__ == "int"):
            arg2 *= 1.0
            
        if (arg2.__class__.__name__ == "float"):
            return v.__mul_Scalar__(arg2)

        print "Vector.__mul__: Invalid second argument: ",arg2.__class__.__name__

    def __rmul__(v,arg2):
        return v*arg2
        

    def __mul_Scalar__(v,c):
        #Vector with Scalar: Vector
        u=Vector(v)

        for i in range( len(v) ):
            u[i] *= c

        return u
    
    def __mul_Vector__(v,w):
        #Vector with Vector: Scalar
        dot=0.0

        for i in range( len(v) ):
            dot += v[i]*w[i]
            
        return dot
        
    def __imul__(v,w):
        #Unary multiplication: u=*v
        return v*w

    def __str__(v):
        #Diferentiate print vectors.
        text = []
        for vi in v:
            text.append( str(vi) )

        return "{"+",".join(text)+"}"

    def DotProduct(v,w):
        return v*w
    
    def SqLength(v):
        return v*v
    
    def Length(v):
        return sqrt( v.SqLength() )
    
    def Normalize(v,length=1.0):
        w = Vector()
        if (v.Length()>0.0):
            w = v*(1.0/v.Length())
    
    def Hat2(v):
        return Vector([ -v[1],v[0] ])

    def Projection(v,e):
        return e*(v*e)/e.SqLength()
    
    def Complement(v,e):
        return v-v.Projection(e)

    def Map_Affin(v,A,B=None):
        u = Vector( len(v) )

        for i in range( len(v) ):
            u[i] = 0.0
            for j in range( len(v) ):
                u[i] += A[i][j]*v[j]
                if (B):
                    u[i] += B[j]
                   
        return u


def O():
    #Origin
    return Vector([0.0,0.0])

#Unit Vectors

def i():
    return Vector([1.0,0.0])

def j():
    #i's complement (normal)
    return Vector([0.0,1.0])

def e(t):
    return Vector([
        cos(t),
        sin(t)
    ])

def f(t):
    #e's complement (normal)
    return Vector([
        -sin(t),
        cos(t)
    ])

def p(t):
    return Vector([
        cos(t),
        -sin(t)
    ])

def q(t):
    #q's complement (normal)
    return Vector([
        sin(t),
        cos(t)
    ])


def Map_Affin_Vectors(ps,A,B=None,tell=0):
    rps=[]
    for p in ps:
        rps.append(   p.Map_Affin(A,B)   )
        if (tell): print p,"-->",p.Map_Affin(A,B)

    return rps