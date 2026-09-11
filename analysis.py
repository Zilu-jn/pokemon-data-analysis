# Analyze Pokémon statistics with Pandas.

import pandas as pd
import matplotlib.pyplot as plt

# Import the Dataset
DATA_PATH = "data/Pokemon.csv"

pokemon = pd.read_csv(DATA_PATH)

# Inspect the Data
print("First five rows:")
print(pokemon.head())

print("\nDataset shape:")
print(pokemon.shape)

print("\nColumn names:")
print(pokemon.columns.tolist())

print("\nDataset information:")
pokemon.info()

print("\nSummary statistics:")
print(pokemon.describe())

# Checking for missing values and duplicates
print("\nMissing values:")
print(pokemon.isna().sum())

print("\nNumber of duplicate rows:")
print(pokemon.duplicated().sum())

# Filtering Pokémon with Attack of 120 or higher
strong_pokemon = pokemon[pokemon["Attack"] >= 120]
print("\nPokémon with Attack of 120 or higher:")
print(strong_pokemon[["Name", "Type 1", "Attack"]].head(10))

print("\nNumber of Pokémon with Attack of 120 or higher:")
print(len(strong_pokemon))

# Group Pokémon by primary type
pokemon_count_by_type = pokemon.groupby("Type 1")["Name"].count()
print("\nNumber of Pokémon by primary type:")
print(pokemon_count_by_type)

average_attack_by_type = pokemon.groupby("Type 1")["Attack"].mean()
print("\nAverage Attack by primary type:")
print(average_attack_by_type.round(2))

# Create a bar chart of average Attack by type
sorted_attack = average_attack_by_type.sort_values()

sorted_attack.plot(kind="barh", color="steelblue")

plt.title("Average Pokémon Attack by Primary Type")
plt.xlabel("Average Attack")
plt.ylabel("Primary Type")
plt.tight_layout()

plt.savefig("images/average_attack_by_type.png")
plt.show()
