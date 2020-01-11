import numpy as np
# Rain, Sunny, Cloudy

P = np.asarray([ [0.5, 0.25, 0.25]
                ,[0.5, 0,    0.5]
                ,[0.25,0.25, 0.5]], dtype = float)

init_vector1 = np.asarray([0, 1, 0], dtype = float)
init_vector2 = np.asarray([1, 0, 0], dtype = float)
init_vector3 = np.asarray([0, 0, 1], dtype = float)

num = 10

for i in range(num):
    init_vector1 = np.dot(init_vector1, P)
    init_vector2 = np.dot(init_vector2, P)
    init_vector3 = np.dot(init_vector3, P)

print('vector1(rain) = ',init_vector1)
print('vector2(sunny) = ',init_vector2)
print('vector3(cloudy) = ',init_vector3)
