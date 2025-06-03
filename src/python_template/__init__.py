import os

from dotenv import find_dotenv, load_dotenv
from loguru import logger

from bar.fibonacci import fib
from foo.calculator import multiply

_ = load_dotenv(find_dotenv(".env.shared"), override=True)
_ = load_dotenv(find_dotenv(".env.local"), override=True)


def main() -> None:
    logger.info("main() enter")
    default_user = ""
    if "DEFAULT_USER" in os.environ:
        default_user = os.getenv("DEFAULT_USER")
        print(os.getenv("AIDER_DARK_MODE"))
        logger.debug(f"default_user: {default_user}")
    else:
        logger.error(
            "DEFAULT_USER not available in environ variable, please specify it in '.env.shared' or '.env.local' or environment variables. Exit..."
        )
        exit(1)
    print(f"Hello from python-template, {default_user}!")
    print(multiply(fib(10), fib(20)))
    logger.info("main() exit")
