import pandas as pd
from TestJson import main
df = pd.read_json("C:\\Users\\1716293.RGU.000\\Clustering-Bin-Packing\\src\\main\\resources\\loads_temp.json")
# clusters = int(input("how many clusters?\n"))
bins = main(df)
print(bins)