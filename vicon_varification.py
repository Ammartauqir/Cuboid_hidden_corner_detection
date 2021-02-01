import pandas as pd
data_2D_projected = pd.read_csv("box_positions_2D.csv")
data_3D_projected = pd.read_csv("box_positions_normalized.csv")
df = pd.DataFrame(data_3D_projected, columns=['VarName2'])
print(data_3D_projected)
