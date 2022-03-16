import pandas as pd
import numpy as np


numpyArray = np.array([3. , '?', 2. , 5. , '*' , 4. , 5. , 6. , '+' , 3., 2. , '&' , 5. , '?' , 7. , '!']).reshape(4,4)

df = pd.DataFrame(numpyArray, columns=['column_1','column_2','column_3','column_4'])
print(df)
