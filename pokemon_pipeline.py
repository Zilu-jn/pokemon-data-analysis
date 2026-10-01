from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def load_pokemon_data(path: str | Path = "data/Pokemon.csv") -> pd.DataFrame:
    """Load Pokémon data from a CSV file."""
    return pd.read_csv(path)


# Part 1: Core function - calculate average Attack by primary type
def calculate_average_attack_by_type(pokemon: pd.DataFrame) -> pd.Series:
    return pokemon.groupby("Type 1")["Attack"].mean()


# Part 1: Core function - filter Pokémon by Attack
def filter_strong_pokemon(
    pokemon: pd.DataFrame, minimum_attack: int = 120
) -> pd.DataFrame:
    return pokemon[pokemon["Attack"] >= minimum_attack]


# Repository A - W4: Find unusual Attack values with the IQR method
def find_attack_outliers(pokemon: pd.DataFrame) -> pd.DataFrame:
    """Return Pokémon whose Attack values are outside the IQR limits."""
    first_quartile = pokemon["Attack"].quantile(0.25)
    third_quartile = pokemon["Attack"].quantile(0.75)
    iqr = third_quartile - first_quartile

    lower_limit = first_quartile - 1.5 * iqr
    upper_limit = third_quartile + 1.5 * iqr

    return pokemon[
        (pokemon["Attack"] < lower_limit) | (pokemon["Attack"] > upper_limit)
    ]


# Repository A - W4: Refactoring - extract model training into a function
def train_legendary_model(pokemon: pd.DataFrame):
    """Train a decision tree and return its accuracy and predictions."""
    feature_columns = [
        "HP",
        "Attack",
        "Defense",
        "Sp. Atk",
        "Sp. Def",
        "Speed",
    ]
    model_inputs = pokemon[feature_columns]
    model_output = pokemon["Legendary"]

    inputs_train, inputs_test, output_train, output_test = train_test_split(
        model_inputs,
        model_output,
        test_size=0.2,
        random_state=42,
        stratify=model_output,
    )

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(inputs_train, output_train)

    predictions = model.predict(inputs_test)
    accuracy = accuracy_score(output_test, predictions)

    prediction_results = pd.DataFrame(
        {
            "Actual": output_test,
            "Predicted": predictions,
        }
    )

    return accuracy, prediction_results
