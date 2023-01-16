import toolz
from pandas import DataFrame


@toolz.curry
def execute(command: str, df: DataFrame) -> float:
    """Execute calculation of some metric (mean, variance, max, min)."""
    match command:
        case "mean":
            return df.AverageTemperature.mean()
        case "variance":
            return df.AverageTemperature.var()  # type: ignore
        case "max":
            return df.AverageTemperature.max()
        case "min":
            return df.AverageTemperature.min()
        case _:
            raise Exception("Invalid command")
