import numpy as np
class GBM:
    """
    A class to simulate Geometric Brownian Motion paths.
    
    Geometric Brownian Motion follows the equation:
    dY = mu*Ydt + sigma*SdB
    
    where:
    - (mu) is the drift coefficient
    - (sigma) is the volatility
    - B is the brownian motion
    """
    def __init__(self,Y0,mu,sigma):
        """
        Initialize GBM parameters.
        
        Parameters:
        -----------
        Y0 : float
            Initial asset price
        mu : float
            Drift coefficient (expected return)
        sigma : float
            Volatility (standard deviation)
        T : float
            Total time period
        """
        self.Y0=Y0
        self.mu=mu
        self.sigma=sigma

    def simulate_path(self,T,N):
        self.T=T
        self.N=N  
        self.dt= self.T/self.N 
        Y_t= np.exp(
            (self.mu-self.sigma**2/2)*self.dt
            +self.sigma*np.random.normal(0,np.sqrt(self.dt),size=(self.N))
        )
        Y_t= self.Y0*np.cumprod(np.insert(Y_t,0,1.))

        return np.linspace(0,self.T,self.N+1),Y_t
