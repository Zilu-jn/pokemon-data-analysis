from pathlib import Path

import pandas as pd


def load_pokemon_data(path: str | Path = "data/Pokemon.csv") -> pd.DataFrame:
    """Load Pokémon data from a CSV file."""
    return pd.read_csv(path)


# Part 1: Core function — calculate average Attack by primary type
def calculate_average_attack_by_type(pokemon: pd.DataFrame) -> pd.Series:
    return pokemon.groupby("Type 1")["Attack"].mean()


# Part 1: Core function — filter Pokémon by Attack
def filter_strong_pokemon(
    pokemon: pd.DataFrame, minimum_attack: int = 120
) -> pd.DataFrame:
    return pokemon[pokemon["Attack"] >= minimum_attack]
