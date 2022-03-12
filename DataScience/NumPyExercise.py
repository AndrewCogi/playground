# NumPy Coding Exercise
import numpy as np

# create a wt array with 100 random float numbers between 40.0 and 90.0
wt=np.round(np.random.uniform(40,90,100),1)

# create a ht array with 100 random integer numbers between 140 and 200
ht=np.array(np.random.randint(140,201,100))

# compute the BMI for the 100 students, store them in a bmi array
bmi=wt/((ht/100)*(ht/100))

# print bmi array (first 10 elements of the bmi array)
print(bmi[:10])
