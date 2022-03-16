import pandas as pd
import numpy as np

# Create a Pandas (4,4) DataFrame
df = pd.DataFrame({
    'column_a':[3. , '?' , 2. , 5.],
    'column_b':['*' , 4. , 5. , 6.],
    'column_c':['+' , 3. , 2. , '&'],
    'column_d':[5. , '?' , 7. , '!']})

# Display the DataFrame
print(df)

# Replace any non-numeric value with NaN
df.replace({'?':np.NaN, '*':np.NaN, '+':np.NaN, '&':np.NaN, '!':np.NaN}, inplace=True)

# Display the DataFrame
print(df)
