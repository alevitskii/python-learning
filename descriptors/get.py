from __future__ import annotations

import logging
from typing import ClassVar, Self, overload, reveal_type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DescriptorClass[T]:
    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...

    @overload
    def __get__(self, instance: T, owner: type[T] | None = None) -> T: ...

    def __get__(self, instance: T | None, owner: type[T] | None = None) -> T | Self:
        if instance is None:
            logger.info(
                f"{self.__class__.__name__}.{owner.__name__ if owner else 'None'}"
            )
            # usually self is returned if called from the class
            return self
        logger.info(
            "Call: %s.__get__(%r, %r)",
            self.__class__.__name__,
            instance,
            owner,
        )
        return instance


class ClientClass:
    # Must be a class attribute, not an instance attribute.
    # NOTE: There are some differences in how Mypy and Pyright understand class vars
    # https://github.com/microsoft/pyright/issues/4837#issuecomment-1482997680
    descriptor: ClassVar = DescriptorClass[Self]()


def main() -> None:
    client = ClientClass()
    print(client.descriptor)
    reveal_type(client.descriptor)
    print(client.descriptor is client)
    print(ClientClass.descriptor)


if __name__ == "__main__":
    main()
