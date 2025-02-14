from typing import Generic, TypeVar


class Refuse:
    """Any refuse."""


class Biodegradable(Refuse):
    """Biodegradable refuse."""


class Compostable(Biodegradable):
    """Compostable refuse."""


T_contra = TypeVar("T_contra", contravariant=True)


class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        """Store trash until dumped."""


def deploy(trash_can: TrashCan[Biodegradable]) -> None:
    """Deploy a trash can for biodegradable refuse."""


bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can)

compost_can: TrashCan[Compostable] = TrashCan()
# Argument 1 to "deploy" has incompatible type "TrashCan[Compostable]" expected "TrashCan[Biodegradable]"
deploy(compost_can)  # type: ignore
