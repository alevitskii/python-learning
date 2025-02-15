# Always use functools.wraps when decorating
import logging
from collections.abc import Callable
from functools import wraps

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class ControlledException(Exception):
    """A generic exception on the program's domain."""


def retry[**P, R](operation: Callable[P, R], /) -> Callable[P, R]:
    @wraps(operation)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised

    return wrapped


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


# retry(run_operation)(*args, **kwargs) == wrapped(*args, **kwargs)
@retry
def run_operation(task: RunWithFailure) -> int:
    """Run a particular task, simulating some failures on its execution."""
    return task.run()


def main() -> None:
    operationObj = OperationObject()
    tester = RunWithFailure(operationObj, fail_n_times=3)
    run_operation(tester)


if __name__ == "__main__":
    main()
