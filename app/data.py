import pathlib
import zipfile

import pandas as pd
import requests


def parse_weather(path: pathlib.Path) -> pd.DataFrame:  # noqa
    """Try find `archive.zip` or `GlobalLandTemperaturesByMajorCity.csv` and parse it.

    Args:
        path (pathlib.Path): file to open.

    Returns:
        pd.DataFrame: DataFrame of weather.
    """
    if path.suffix == ".csv":
        return pd.read_csv(path, parse_dates=["dt"])
    elif path.suffix == ".zip":
        with zipfile.ZipFile(path) as z:
            with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
                return pd.read_csv(f, parse_dates=["dt"])
    else:
        raise Exception(f"Wrong path: {path}")


def _convert_longitude(value: str) -> float:
    return -float(value[:-1]) if value[-1] == "W" else float(value[:-1])  # noqa


def _convert_latitude(value: str) -> float:
    return -float(value[:-1]) if value[-1] == "S" else float(value[:-1])  # noqa


def convert_position(df: pd.DataFrame) -> pd.DataFrame:
    """Convert latitude and longitude to numbers."""
    df.Latitude = df.Latitude.map(_convert_latitude)
    df.Longitude = df.Longitude.map(_convert_longitude)
    return df
