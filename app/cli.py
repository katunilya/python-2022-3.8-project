import pathlib
from datetime import datetime
from typing import Literal, Optional

import pandas as pd
import typer
from toolz import pipe

from app import command, data, filters

cli = typer.Typer(
    name="weather",
    no_args_is_help=True,
)


@cli.command()
def run(
    cmd: str = typer.Argument(default="mean"),  # noqa
    source: Optional[pathlib.Path] = typer.Option(None),  # noqa
    city: Optional[str] = typer.Option(None),  # noqa
    country: Optional[str] = typer.Option(None),  # noqa
    from_date: Optional[datetime] = typer.Option(None),  # noqa
    to_date: Optional[datetime] = typer.Option(None),  # noqa
    from_latitude: Optional[float] = typer.Option(None),  # noqa
    to_latitude: Optional[float] = typer.Option(None),  # noqa
    from_longitude: Optional[float] = typer.Option(None),  # noqa
    to_longitude: Optional[float] = typer.Option(None),  # noqa
):
    """Perform some calculation with some filtered weather information.

    Args:
        cmd (str): statistics metric to calculate (mean, max, min, variance).
        source (pathlib.Path | None, optional): file with weather info.
        city (str | None): comma-separated string of cities to take.
        country (str | None): comma-separated string of countries to take.
        from_date (datetime | None): date to start from (including).
        to_date (datetime | None): date to stop (including).
        from_latitude (float | None): latitude to start from (including).
        to_longitude (float | None): longitude to stop (including).
        to_latitude (float | None): latitude to start from (including).
        from_longitude (float | None): longitude to stop (including).
    """
    result = pipe(
        pathlib.Path().cwd() if source is None else source,
        data.parse_weather,
        data.convert_position,
        filters.city(city),
        filters.country(country),
        filters.from_date(from_date),
        filters.to_date(to_date),
        filters.from_latitude(from_latitude),
        filters.to_latitude(to_latitude),
        filters.from_longitude(from_longitude),
        filters.to_longitude(to_longitude),
        command.execute(cmd),
    )

    typer.echo(result)
