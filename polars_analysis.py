# Analyze Pokémon statistics with Polars.
import time

import pandas as pd
import polars as pl

DATA_PATH = "data/Pokemon.csv"

pokemon = pl.read_csv(DATA_PATH)

print("First five rows:")
print(pokemon.head())

average_attack_by_type = (
    pokemon.group_by("Type 1")
    .agg(pl.col("Attack").mean().alias("Average Attack"))
    .sort("Average Attack", descending=True)
)

print("\nAverage Attack by primary type:")
print(average_attack_by_type)


# Compare Pandas and Polars performance
pandas_pokemon = pd.read_csv(DATA_PATH)
repetitions = 1000
start_time = time.perf_counter()

for _ in range(repetitions):
    pandas_pokemon.groupby("Type 1")["Attack"].mean()

pandas_time = time.perf_counter() - start_time
start_time = time.perf_counter()

for _ in range(repetitions):
    pokemon.group_by("Type 1").agg(pl.col("Attack").mean())

polars_time = time.perf_counter() - start_time

print("\nPerformance comparison:")
print("Pandas time:", round(pandas_time, 4), "seconds")
print("Polars time:", round(polars_time, 4), "seconds")
