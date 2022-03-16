import pandas as pd
import numpy as np

# Create (4,4) NumPy array
numpyArray = np.array([3. , '?', 2. , 5. , '*' , 4. , 5. , 6. , '+' , 3., 2. , '&' , 5. , '?' , 7. , '!']).reshape(4,4)

# Create a DataFrame from NumPy array
df = pd.DataFrame(numpyArray, columns=['column_1','column_2','column_3','column_4'])

# Display the DataFrame
print(df, end='\n\n')

# Replace any non-numeric value with NaN
df.replace({'?':np.NaN, '*':np.NaN, '+':np.NaN, '&':np.NaN, '?':np.NaN, '!':np.NaN}, inplace=True)

# Display the DataFrame
print(df)
