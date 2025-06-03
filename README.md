# Python Template

A Python template focused on development speed and best practices, leveraging modern tools for efficient development workflows.

## Features

This template integrates the following key tools and libraries:

- [uv][uv]: A fast Python package installer and resolver.
- [ruff][ruff]: An extremely fast Python linter and formatter.
- [pydantic][pydantic]: Data validation and settings management using Python type hints.
- [pytest][pytest]: A mature full-featured Python testing framework.
- [loguru][loguru]: A library for easy and flexible logging.

## Prerequisites

Ensure you have `uv` installed on your system. If not, you can install it by following the instructions on the [uv documentation][uv].

## Getting Started

To set up the project and install dependencies:

```bash
uv sync
uv run pre-commit install
```

This command will:

1. Synchronize dependencies defined in `pyproject.toml`.
2. Install pre-commit hooks to ensure code quality using [ruff][ruff] before commits.

## Running the Application

To run the main binary module of the project:

```bash
uv run python-template
```

## Testing

### Running Tests

You can run your tests using `uv` and `pytest`:

```bash
uv run pytest
```

To see more detailed output, add the verbose flag (`-v` or `--verbose`):

```bash
uv run pytest -v
```

### Running Tests with Coverage

To run tests and generate a coverage report:

```bash
uv run pytest --cov
```

[uv]: https://docs.astral.sh/uv/
[ruff]: https://docs.astral.sh/ruff/
[pydantic]: https://docs.pydantic.dev/latest/
[pytest]: https://docs.pytest.org/en/stable/
[loguru]: https://loguru.readthedocs.io/en/stable/
