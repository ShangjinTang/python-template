- Python Built-In:
  - Always focus on python version 3.12.
  - Typing System: Use types everywhere possible. Do not use deprecated features. Always follow Python PEP585 and PEP604, do not use deprecated typing types.
  - Path: Use `pathlib` instead of `os` whenever possible.
- Third Party Libraries:
  - `pydantic`: Use pydantic `from pydantic.dataclasses import dataclass` instead of built-in `from dataclasses import dataclass`. Always use pydantic V2, do not use pydantic V1.
  - `loguru`: Do not use python built-in `logging` module. Use logger in `from loguru import logger`.
  - `pytest`: Always use `pytest` instead of python built-in `unittest`.
