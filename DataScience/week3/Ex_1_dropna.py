import pandas as pd
import numpy as np

# Create a Pandas (4,4) DataFrame
df = pd.DataFrame({
    'column_a':[3. , '?' , 2. , 5.],
    'column_b':['*' , 4. , 5. , 6.],
    'column_c':['+' , 3. , 2. , '&'],
    'column_d':[5. , '?' , 7. , '!']})

# Replace any non-numeric value with NaN
df.replace({'?':np.NaN, '*':np.NaN, '+':np.NaN, '&':np.NaN, '?':np.NaN, '!':np.NaN}, inplace=True)

# Display the DataFrame after applying each function (dropna with how any, how all, thresh 1, thresh 2)
# dropna with how any
print(df.dropna(axis=0, how='any', inplace=False))
# dropna with how all
print(df.dropna(axis=0, how='all', inplace=False))
# dropna with thresh 1
print(df.dropna(axis=0, thresh=1, inplace=False))
# dropna with thresh 2
print(df.dropna(axis=0, thresh=2, inplace=False))
