import numpy as np

import array as arr 

a_list = [3, 6, 7, 11]

print(type(a_list)) # <class 'list'>

an_array = arr.array("f", [3.14, 22.43, 14.8, 45.97])

print(type(an_array)) # <class 'array.array'>    

print([(type(i) == float) for i in an_array]) # [True, True, True, True]

a_numpy_array = np.array([45, 212, 878, 987], dtype="float")

print(a_numpy_array) # [ 45. 212. 878. 987.]

cities = ["Izmir", 35, "Istanbul", 34]

print([type(i) for i in cities]) # [<class 'str'>, <class 'int'>, <class 'str'>, <class 'int'>]
