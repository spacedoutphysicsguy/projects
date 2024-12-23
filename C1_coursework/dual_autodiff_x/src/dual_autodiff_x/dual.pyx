import numpy as np

cdef class Dual:
    '''
    Python class to perform automatic differentiation using dual numbers. 
    arguments: 
    a: input value
    b: input slope
    '''

    cdef double a 
    cdef double b
    # Initialisation
    def __init__(self, double a,double b):
        '''
        Initializes a Dual number with a real part and a dual part.
        
        Parameters:
        a (float): The real part of the dual number.
        b (float): The dual part (slope) of the dual number.
        '''
        self.real = a 
        self.dual = b 

    # Defining what to return when a dual object is printed
    def __repr__(self):
        '''
        Returns a string representation of the Dual number for debugging.
        
        Returns:
        str: A string in the format (real, dual).
        '''
        return f"({self.real},{self.dual})"
        
    def __str__(self):
        '''
        Returns a user-friendly string representation of the Dual number.
        
        Returns:
        str: A string in the format Dual(real=real_value, dual=dual_value).
        '''
        return f"Dual(real={self.real},dual={self.dual})"
    
    def __class__(self):
        '''
        Returns the class name of the Dual object.
        
        Returns:
        str: The name of the class.
        '''
        return "Dual"
    
    # Defining arithmetic operations
    def __add__(self, o):
        '''
        Defines addition for Dual numbers.
        
        Parameters:
        o (Dual): Another Dual number to add.
        
        Returns:
        Dual: A new Dual number representing the sum.
        '''
        return Dual(self.real + o.real, self.dual + o.dual)
    
    def __sub__(self, o):
        '''
        Defines subtraction for Dual numbers.
        
        Parameters:
        o (Dual): Another Dual number to subtract.
        
        Returns:
        Dual: A new Dual number representing the difference.
        '''
        return Dual(self.real - o.real, self.dual - o.dual)
    
    def __mul__(self, o):
        '''
        Defines multiplication for Dual numbers.
        
        Parameters:
        o (Dual): Another Dual number to multiply.
        
        Returns:
        Dual: A new Dual number representing the product.
        '''
        return Dual(self.real * o.real, self.dual * o.real + self.real * o.dual)
    
    def __truediv__(self, o):
        '''
        Defines division for Dual numbers.
        
        Parameters:
        o (Dual): Another Dual number to divide by.
        
        Returns:
        Dual: A new Dual number representing the quotient.
        '''
        return Dual(self.real / o.real, (self.dual * o.real - self.real * o.dual) / (o.real ** 2))
    
    def __pow__(self, o):
        '''
        Defines exponentiation for Dual numbers.
        
        Parameters:
        o (Dual or float): The exponent to raise the Dual number to.
        
        Returns:
        Dual: A new Dual number representing the result of exponentiation.
        '''
        if type(o) == type(self):
            return Dual(self.real ** o.real, self.real ** o.real * ((o.real * self.dual) / self.real + o.dual * np.log(self.real)))
        else:
            return Dual(self.real ** o, self.dual * o * self.real ** (o - 1))
    
    # Defining common algebraic operations
    def sin(self):
        '''
        Computes the sine of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the sine value and its derivative.
        '''
        return Dual(np.sin(self.real), self.dual * np.cos(self.real))
    
    def cos(self):
        '''
        Computes the cosine of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the cosine value and its derivative.
        '''
        return Dual(np.cos(self.real), -self.dual * np.sin(self.real))
    
    def tan(self):
        '''
        Computes the tangent of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the tangent value and its derivative.
        '''
        return Dual(np.tan(self.real), self.dual * np.cos(self.real) ** -2)
    
    def log(self):
        '''
        Computes the natural logarithm of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the logarithm value and its derivative.
        '''
        return Dual(np.log(self.real), self.dual / self.real)
    
    def exp(self):
        '''
        Computes the exponential of the Dual number.
        
        Returns:
        Dual: A new Dual number representing exp(x) and its derivative.
        '''
        return Dual(np.exp(self.real), self.dual * np.exp(self.real))
    
    # Defining common activation functions
    def relu(self):
        '''
        Computes the ReLU (Rectified Linear Unit) of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the ReLU value and its derivative.
        '''
        return Dual(max(0, self.real), 1 if self.real > 0 else 0)
    
    def sigmoid(self):
        '''
        Computes the sigmoid of the Dual number.
        
        Returns:
        Dual: A new Dual number representing the sigmoid value and its derivative.
        '''
        sig = 1 / (1 + np.exp(-self.real))
        return Dual(sig, self.dual * sig * (1 - sig))
    


