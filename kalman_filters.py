import numpy as np
def update(n,x,P):
    y = np.array(measurements[n]) - np.dot(H,x)
    s = np.dot(np.dot(H,P),H.transpose()) + R
    k = np.dot(np.dot(P,np.transpose(H)),np.linalg.inv(s))

    x = x + np.dot(k,y)
    P = np.dot((I - np.dot(k,H)),P)

    return [x, P]

def predict(n,x,P):
    x = np.dot(F,x) + u
    P = np.dot(np.dot(F,P),F.transpose())

    return [x,P]


# Implement the filter function below

def kalman_filter(x, P):
    for n in range(len(measurements)):
        x, P = update(n,x,P)
        x, P = predict(n,x,P)
        
    return x,P

############################################
### use the code below to test your filter!
############################################

measurements = [1, 2, 3]

x = np.array([[0.], [0.]]) # initial state (location and velocity)
P = np.array([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = np.array([[0.], [0.]]) # external motion
F = np.array([[1., 1.], [0, 1.]]) # next state function
H = np.array([[1., 0.]]) # measurement function
R = np.array([[1.]]) # measurement uncertainty
I = np.array([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]

