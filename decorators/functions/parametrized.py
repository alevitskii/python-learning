import logging
from collections.abc import Callable, Sequence
from functools import wraps

from simple import ControlledException, OperationObject, RunWithFailure

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

_DEFAULT_RETRIES_LIMIT = 3


def with_retry[**P, R](
    retries_limit: int = _DEFAULT_RETRIES_LIMIT,
    allowed_exceptions: Sequence[type[Exception]] | None = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    allowed_exceptions = (
        tuple(allowed_exceptions) if allowed_exceptions else (ControlledException,)
    )

    def retry(operation: Callable[P, R]) -> Callable[P, R]:
        @wraps(operation)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logger.warning(f"retrying {operation.__qualname__!r} due to {e}")
                    last_raised = e
            raise last_raised

        return wrapped

    return retry


# with_retry()(run_operation)(*args, **kwargs) == retry(run_operation)(*args, **kwargs) == wrapped(*args, **kwargs)
@with_retry()
def run_operation(task: RunWithFailure) -> int:
    return task.run()


@with_retry(retries_limit=5)
def run_with_custom_retries_limit(task: RunWithFailure) -> int:
    return task.run()


@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task: RunWithFailure) -> int:
    return task.run()


@with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError))
def run_with_custom_parameters(task: RunWithFailure) -> int:
    return task.run()


def main() -> None:
    operationObj = OperationObject()
    tester = RunWithFailure(operationObj, fail_n_times=2)
    run_with_custom_retries_limit(tester)


if __name__ == "__main__":
    main()
