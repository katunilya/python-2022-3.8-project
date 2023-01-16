# python-2022-3.8-project

## Usage

After installing dependencies new command line interface will appear. You can interact with that via `weather` command.

For more information invoke:

```sh
weather --help
```

CLI requires `archive.zip` or `GlobalLandTemperaturesByMajorCity.csv` persent in current working directory or being passed as option `--source`.

Example usage:

```sh
weather mean --source ./GlobalLandTemperaturesByMajorCity.csv --from-date 1995-01-23 --city 'Saint Petersburg, Moscow'
```

This command would calculate mean average temperature in Saint Petersburg and Moscow since 23 Jan 1995 (including).

## Setup

Requires `python3.10` and `poetry1.2+`.

- Clone repository

```sh
git clone git@github.com:katunilya/python-2022-3.8-project.git
```

- Create virtual environment

```sh
python3.10 -m venv .venv
source .venv/bin/activate  # unix systems
```

- Install dependencies

```sh
poetry install
```

- Setup pre-commit

```sh
pre-commit install --hook-type pre-commit --hook-type pre-push
```

### Building wheel

Wheel is build via poetry 

```sh
poetry build
```
