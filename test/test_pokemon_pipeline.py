import pytest

from pokemon_pipeline import (
    load_pokemon_data,
    calculate_average_attack_by_type,
    filter_strong_pokemon,
)


# Part 1: Unit test — data loading
def test_load_pokemon_data(tmp_path):
    csv_file = tmp_path / "pokemon.csv"
    csv_file.write_text(
        "Name,Type 1,Attack\n" "Pikachu,Electric,55\n" "Bulbasaur,Grass,49\n",
        encoding="utf-8",
    )

    result = load_pokemon_data(csv_file)

    assert result.shape == (2, 3)
    assert result["Name"].tolist() == ["Pikachu", "Bulbasaur"]
    assert result["Attack"].tolist() == [55, 49]


# Part 1: Unit test — missing-file edge case
def test_load_pokemon_data_missing_file(tmp_path):
    missing_file = tmp_path / "does_not_exist.csv"

    with pytest.raises(FileNotFoundError):
        load_pokemon_data(missing_file)


# Part 1: Unit test — average Attack calculation
def test_calculate_average_attack_by_type():
    import pandas as pd

    pokemon = pd.DataFrame(
        {
            "Type 1": ["Fire", "Fire", "Water"],
            "Attack": [80, 100, 60],
        }
    )

    result = calculate_average_attack_by_type(pokemon)

    assert result["Fire"] == 90
    assert result["Water"] == 60


# Part 1: Unit test — filter strong Pokémon
def test_filter_strong_pokemon():
    import pandas as pd

    pokemon = pd.DataFrame(
        {
            "Name": ["Pikachu", "Dragonite", "Charizard"],
            "Attack": [55, 134, 84],
        }
    )

    result = filter_strong_pokemon(pokemon)

    assert result["Name"].tolist() == ["Dragonite"]


# Part 1: System/integration test — run the complete analysis
def test_complete_analysis():
    import os
    import subprocess
    import sys
    from pathlib import Path

    project_folder = Path(__file__).resolve().parents[1]
    environment = os.environ.copy()
    environment["MPLBACKEND"] = "Agg"

    result = subprocess.run(
        [sys.executable, "analysis.py"],
        cwd=project_folder,
        env=environment,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Dataset shape:" in result.stdout
    assert "Model accuracy:" in result.stdout
    assert (project_folder / "images/average_attack_by_type.png").is_file()
