import numpy as np

class HCWLTIDynamics(object):
    def __init__(self, r0 = 6793137, fthr = 2, m = 4, dt = 0.01):
        # r0 := orbit radius; initial value for r0 is for a satellite in LEO
        # m:= mass in kg
        # fthr in 
        mu = 3.986E14 # m^3/s^2 
        n = np.sqrt(mu/r0**3)
        cos = np.cos(n * dt)
        sin = np.sin(n * dt)
        self.A = np.array([
            [4 - 3 * cos, 0, 0, sin / n, 2/n * (1 - cos), 0],
            [6 * (sin - n * dt), 1, 0, -2/n * (1 - cos), 1/n*(4 * sin - 3 * n * dt), 0],
            [0, 0, cos, 0, 0, 1/n * sin],
            [3 * n * sin, 0, 0, cos, 2 * sin, 0],
            [-6 * n * (1-cos), 0, 0, -2 * sin, 4 * cos - 3, 0],
            [0, 0, -n * sin, 0, 0, cos]
        ])
        self.B = fthr / m * np.array([
            [1/n**2 * (1 - cos), 2/n**2 * (n * dt - sin), 0],
            [-2/n**2 * (n * dt - sin), 4/n**2 * (1- cos) - 3.0/2.0 * dt**2, 0],
            [0, 0, 1/n**2 * (1-cos)],
            [1/n*sin, 1/n*(1 - cos), 0],
            [-2/n*(1-cos), 4/n*sin - 3*dt, 0],
            [0, 0, 1/n*sin]
        ])
        self.C = np.eye(3)
        self.D = np.zeros((3,3))
        # print("HCW Dynamics initialized")

    def step(self, x, u):
        # Input:
        # state x, a (6,) numpy array
        # control input u, a (3,) numpy array
        # Output:
        # xnext, the next state at t + dt, a (6,) numpy array
        return self.A.dot(x) + self.B.dot(u)
# class Sim(object):
#     """docstring for Sim"""
#     def __init__(self, x0):
#         super(Sim, self).__init__()
#         # hold the history of true state variables 
#         self.xtrue = x0
#         self.xtrues = []
        
#         # hold the history of actuator commands and K matrices
#         self.us = []
#         self.Ks = []

#         # hold the history of state estimates and covariance
#         self.xhat = None # xtrue plus sensor noise v
#         self.Xhats = []
#         self.Ps = []


#     def stepsim(self):
#         pass

#     def 
        
if __name__=="__main__":
    print("Main")
    sim = Sim()
    print(sim.A)
    