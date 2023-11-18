import pandas as pd
import numpy as np

df_location = pd.DataFrame(
    np.random.rand(100, 2) + [100, 100],
    columns=["lat", "lon"],
)
print(df_location)
