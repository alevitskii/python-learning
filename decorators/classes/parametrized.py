import logging
from collections.abc import Callable, Sequence
from functools import wraps

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

_DEFAULT_RETRIES_LIMIT = 3


class ControlledException(Exception):
    """A generic exception on the program's domain."""


class OperationObject:
    """A helper object to test the decorator."""

    def __init__(self) -> None:
        self._times_called: int = 0

    def run(self) -> int:
        """Base operation for a particular action"""
        self._times_called += 1
        return self._times_called

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    __repr__ = __str__


class RunWithFailure:
    def __init__(
        self,
        task: OperationObject,
        fail_n_times: int = 0,
        exception_cls: type[Exception] = ControlledException,
    ) -> None:
        self._task = task
        self._fail_n_times = fail_n_times
        self._times_failed = 0
        self._exception_cls = exception_cls

    def run(self) -> int:
        called = self._task.run()
        if self._times_failed < self._fail_n_times:
            self._times_failed += 1
            raise self._exception_cls(f"task failed {self._times_failed} times")
        return called


class WithRetry:
    def __init__(
        self,
        retries_limit: int = _DEFAULT_RETRIES_LIMIT,
        allowed_exceptions: Sequence[type[Exception]] | None = None,
    ) -> None:
        self.retries_limit = retries_limit
        self.allowed_exceptions = (
            tuple(allowed_exceptions) if allowed_exceptions else (ControlledException,)
        )

    def __call__[**P, R](self, operation: Callable[P, R]) -> Callable[P, R]:
        @wraps(operation)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    logger.warning("retrying %s due to %s", operation.__qualname__, e)
                    last_raised = e
            raise last_raised

        return wrapped


@WithRetry(retries_limit=5)
def run_with_custom_retries_limit(task: RunWithFailure) -> int:
    return task.run()


def main() -> None:
    operationObj = OperationObject()
    tester = RunWithFailure(operationObj, fail_n_times=2)
    run_with_custom_retries_limit(tester)


if __name__ == "__main__":
    main()
