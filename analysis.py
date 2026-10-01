# Analyze Pokémon statistics with Pandas.

import matplotlib.pyplot as plt

from pokemon_pipeline import (
    load_pokemon_data,
    calculate_average_attack_by_type,
    filter_strong_pokemon,
    train_legendary_model,
    find_attack_outliers,
)

# Import the Dataset
DATA_PATH = "data/Pokemon.csv"

pokemon = load_pokemon_data(DATA_PATH)

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

# Repository A - W4: Review Attack outliers before deciding how to treat them
attack_outliers = find_attack_outliers(pokemon)

print("\nNumber of Attack outliers:")
print(len(attack_outliers))

print("\nAttack outlier examples:")
print(attack_outliers[["Name", "Type 1", "Attack"]].head(10))

# Filtering Pokémon with Attack of 120 or higher
strong_pokemon = filter_strong_pokemon(pokemon)
print("\nPokémon with Attack of 120 or higher:")
print(strong_pokemon[["Name", "Type 1", "Attack"]].head(10))

print("\nNumber of Pokémon with Attack of 120 or higher:")
print(len(strong_pokemon))

# Group Pokémon by primary type
pokemon_count_by_type = pokemon.groupby("Type 1")["Name"].count()
print("\nNumber of Pokémon by primary type:")
print(pokemon_count_by_type)

average_attack_by_type = calculate_average_attack_by_type(pokemon)
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


# Repository A - W4: Use the refactored model function
accuracy, prediction_results = train_legendary_model(pokemon)

print("\nModel accuracy:")
print(round(accuracy, 2))

print("\nFirst 10 model predictions:")
print(prediction_results.head(10))
