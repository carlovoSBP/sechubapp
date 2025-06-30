from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


def main(name: str = "no_name") -> None:
    logger.info(f"Hello, {name}!")


@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: LambdaContext) -> None:
    name = event.get("name", "no_name")
    main(name)
