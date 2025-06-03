# Python Template

Python template focus on tool speed and best practice.

- [uv][uv]
- [ruff][ruff]
- [pydantic][pydantic]
- [pytest][pytest]
- [loguru][loguru]

## Prerequisites

Install [uv][uv].

## Running Binary Module

```bash
uv sync
uv run pre-commit install
uv run python-template
```

This will sync dependencies in [pyproject.toml](./pyproject.toml).

```bash
```

## Testing

### Running Tests

Now you can run your tests using uv:

```bash
uv run pytest
```

To see more detailed output, add the verbose flag `-v|--verbose`.

## Running Tests with Coverage

```bash
uv run pytest --cov
```

[uv]: https://docs.astral.sh/uv/
[ruff]: https://docs.astral.sh/ruff/
[pydantic]: https://docs.pydantic.dev/latest/
[pytest]: https://docs.pytest.org/en/stable/
[loguru]: https://loguru.readthedocs.io/en/stable/
