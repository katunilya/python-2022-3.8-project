# type: ignore
import pathlib
from datetime import datetime

import pandas as pd
import pytest
from toolz import pipe

from app import data, filters


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.read_csv(
        pathlib.Path().cwd() / "tests" / "GlobalLandTemperaturesByMajorCity.csv",
        parse_dates=["dt"],
    )


@pytest.mark.parametrize(
    "city, target",
    [
        ("Saint Petersburg", ["Saint Petersburg"]),
        ("Moscow", ["Moscow"]),
        ("Saint Petersburg, Moscow", ["Moscow", "Saint Petersburg"]),
        ("Saint Petersburg,Moscow", ["Moscow", "Saint Petersburg"]),
        (" Saint Petersburg,Moscow ", ["Moscow", "Saint Petersburg"]),
    ],
)
def test_city(df: pd.DataFrame, city: str, target: list[str]):
    df = filters.city(city, df)  # noqa
    assert df.City.isin(target).all()


@pytest.mark.parametrize(
    "country, target",
    [
        ("Russia", ["Russia"]),
        ("Ethiopia", ["Ethiopia"]),
        ("Ethiopia, Russia", ["Ethiopia", "Russia"]),
        ("Ethiopia,Russia", ["Ethiopia", "Russia"]),
        (" Ethiopia, Russia ", ["Ethiopia", "Russia"]),
    ],
)
def test_country(df: pd.DataFrame, country: str, target: list[str]):
    df = filters.country(country, df)  # noqa
    assert df.Country.isin(target).all()


@pytest.mark.parametrize(
    "from_date, to_date, target_from_date, target_to_date",
    [
        (None, None, datetime(1743, 11, 1), datetime(2013, 9, 1)),
        (
            datetime(2000, 1, 1),
            None,
            datetime(2000, 1, 1),
            datetime(2013, 9, 1),
        ),  # noqa
        (
            None,
            datetime(1999, 12, 31),
            datetime(1743, 11, 1),
            datetime(1999, 12, 31),
        ),  # noqa
        (
            datetime(1990, 1, 1),
            datetime(1999, 12, 31),
            datetime(1990, 1, 1),
            datetime(1999, 12, 31),
        ),
    ],
)
def test_date(
    df: pd.DataFrame,
    from_date: datetime,
    to_date: datetime,
    target_from_date: datetime,
    target_to_date: datetime,
):
    df = pipe(  # noqa
        df,
        filters.from_date(from_date),
        filters.to_date(to_date),
    )
    assert df.dt.max() <= target_to_date
    assert df.dt.min() >= target_from_date


@pytest.mark.parametrize("from_latitude", [0, 10, 25, 50])
def test_from_latitude(
    df: pd.DataFrame,
    from_latitude: float,
):
    df = pipe(  # noqa
        df,
        data.convert_position,
        filters.from_latitude(from_latitude),
    )
    assert df.Latitude.min() >= from_latitude


@pytest.mark.parametrize("to_latitude", [0, 10, 25, 50])
def test_to_latitude(
    df: pd.DataFrame,
    to_latitude: float,
):
    df = pipe(  # noqa
        df,
        data.convert_position,
        filters.to_latitude(to_latitude),
    )
    assert df.Latitude.max() <= to_latitude


@pytest.mark.parametrize("from_longitude", [0, 10, 25, 50])
def test_from_longitude(
    df: pd.DataFrame,
    from_longitude: float,
):
    df = pipe(  # noqa
        df,
        data.convert_position,
        filters.from_longitude(from_longitude),
    )
    assert df.Longitude.min() >= from_longitude


@pytest.mark.parametrize("to_longitude", [0, 10, 25, 50])
def test_to_longitude(
    df: pd.DataFrame,
    to_longitude: float,
):
    df = pipe(  # noqa
        df,
        data.convert_position,
        filters.to_longitude(to_longitude),
    )
    assert df.Longitude.max() <= to_longitude
