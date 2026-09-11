# Analyze Pokémon statistics with Pandas.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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


# Select the model inputs and output
feature_columns = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
X = pokemon[feature_columns]
y = pokemon["Legendary"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Create and train a decision tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the predictions
accuracy = accuracy_score(y_test, predictions)

print("\nModel accuracy:")
print(round(accuracy, 2))

# Compare some actual values with the model predictions
prediction_results = pd.DataFrame(
    {
        "Actual": y_test,
        "Predicted": predictions,
    }
)
print("\nFirst 10 model predictions:")
print(prediction_results.head(10))
