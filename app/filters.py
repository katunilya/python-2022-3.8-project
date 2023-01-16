from datetime import datetime

import pandas as pd
import toolz


@toolz.curry
def from_date(date: datetime | None, df: pd.DataFrame) -> pd.DataFrame:
    """If date is not None return filtered DataFrame."""
    return df[df.dt >= date] if date is not None else df


@toolz.curry
def to_date(date: datetime | None, df: pd.DataFrame) -> pd.DataFrame:
    """If date is not None return filtered DataFrame."""
    return df[df.dt <= date] if date is not None else df


@toolz.curry
def city(city: str | None, df: pd.DataFrame) -> pd.DataFrame:
    """If city is not None return filtered DataFrame."""
    if city is None:
        return df

    cities = toolz.pipe(
        city.split(","),
        toolz.curried.map(str.strip),
        list,
    )
    return df[df.City.isin(cities)]


@toolz.curry
def country(country: str | None, df: pd.DataFrame) -> pd.DataFrame:
    """If country is not None return filtered DataFrame."""
    if country is None:
        return df

    cities = toolz.pipe(
        country.split(","),
        toolz.curried.map(str.strip),
        list,
    )
    return df[df.Country.isin(cities)]


@toolz.curry
def from_latitude(from_latitude: float, df: pd.DataFrame) -> pd.DataFrame:
    """If from_latitude is not None return filtered DataFrame."""
    return df[df.Latitude >= from_latitude] if from_latitude is not None else df


@toolz.curry
def to_latitude(to_latitude: float, df: pd.DataFrame) -> pd.DataFrame:
    """If to_latitude is not None return filtered DataFrame."""
    return df[df.Latitude <= to_latitude] if to_latitude is not None else df


@toolz.curry
def from_longitude(from_longitude: float, df: pd.DataFrame) -> pd.DataFrame:
    """If from_longitude is not None return filtered DataFrame."""
    return df[df.Longitude >= from_longitude] if from_longitude is not None else df


@toolz.curry
def to_longitude(to_longitude: float, df: pd.DataFrame) -> pd.DataFrame:
    """If to_longitude is not None return filtered DataFrame."""
    return df[df.Longitude <= to_longitude] if to_longitude is not None else df
