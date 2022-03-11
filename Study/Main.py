# NumPy Coding Exercise
import numpy as np

# create a wt array with 100 random float numbers between 40.0 and 90.0
wt=np.round(np.array(np.random.random(100)*50+40),1)

# create a ht array with 100 random integer numbers between 140 and 200
ht=np.round(np.array(np.random.random(100)*60+140))
ht=ht.astype(dtype='int64')

#compute the BMI for the 100 students, store them in a bmi array
bmi=wt/((ht/100)*(ht/100))

# print bmi array
print(bmi)


# MatPlotLib Coding Exercise
import matplotlib.pyplot as plt
