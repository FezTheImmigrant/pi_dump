import numpy as np

class ConditionMatrix():
    def __init__(self,initial_point,movement_conditions,landmark_conditions):
        self.__movement_conditions = np.array(movement_conditions)
        self.__landmark_conditions = np.array(landmark_conditions)
        self.__initial_point = initial_point

    def generate_mu(self):
        condition_template = np.array([(1,-1),(-1,1)])
        ##condition_template = np.array([(1,1),(1,1)],[(-1,-1),(-1,-1)],[(-1,-1),(-1,-1)],[(1,1),(1,1)])

        ## (initial positions, movements, landmarks) * 2 for x and y
        shape = 1 + self.__movement_conditions.shape[0] + self.__landmark_conditions.shape[0]
        omega = np.zeros((shape,shape))
        xi = np.zeros((shape,1))

        ##initial position
        omega[0][0] +=1
        xi[0][0] = self.__initial_point


        ##movement conditions
        for i in range(len(self.__movement_conditions)):
            omega[i][i] = omega[i][i] + condition_template[0][0]
            omega[i][i+1] = omega[i][i+1] + condition_template[0][1]

            omega[i+1][i] = omega[i+1][i] + condition_template[1][0]
            omega[i+1][i+1] = omega[i+1][i+1] + condition_template[1][1]

            xi[i][0] = xi[i][0] - self.__movement_conditions[i]
            xi[i+1][0] = xi[i+1][0] + self.__movement_conditions[i]
        
        ##landmark conditions
        for j in range(self.__landmark_conditions.shape[0]):
            landmark_index = len(self.__movement_conditions) + j + 1
            for k in range(self.__landmark_conditions.shape[1]):

                omega[k][k] = omega[k][k] + 1
                omega[k][landmark_index] = omega[k][landmark_index] - 1

                omega[landmark_index][k] = omega[landmark_index][k] -1
                omega[landmark_index][landmark_index] = omega[landmark_index][landmark_index]  + 1

                xi[k][0] = xi[k][0] - self.__landmark_conditions[j][k]
                xi[landmark_index][0] = xi[landmark_index][0] + self.__landmark_conditions[j][k]

        print(omega)



        print (np.linalg.inv(omega).dot(xi))
    



ConditionMatrix(-3,[5,3],[[10,5,1]]).generate_mu()
