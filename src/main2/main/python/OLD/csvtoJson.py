import csv
import json
import pandas as pd

df = pd.read_csv("C:\\Users\\Ashish Upadhyay\\Desktop\\Summer_Internship\\Clustering-Bin-Packing\\src\\main\\resources\\loads_final.csv")
df.to_json("C:\\Users\\Ashish Upadhyay\\Desktop\\Summer_Internship\\Clustering-Bin-Packing\\src\\main\\resources\\loads_temp.json")
df = pd.read_json("C:\\Users\\Ashish Upadhyay\\Desktop\\Summer_Internship\\Clustering-Bin-Packing\\src\\main\\resources\\loads_temp.json")
print(df.head())
df2 = df[:10]
df2.to_json("C:\\Users\\Ashish Upadhyay\\Desktop\\Summer_Internship\\Clustering-Bin-Packing\\src\\main\\resources\\loads_temp1.json")