import pandas as pd
from utils.generic import mean_array, min_max, get_column
df = pd.read_csv("data.csv")
math_scores = get_column(df, "math")
english_scores = get_column(df, "english")
print("Math mean:", mean_array(math_scores))
print("English mean:", mean_array(english_scores))
print("Math min/max:", min_max(math_scores))
print("English min/max:", min_max(english_scores))
df["average"] = (df["math"] + df["english"]) / 2
best = df.loc[df["average"].idxmax()]
print("\nBest student:")
print(best)
