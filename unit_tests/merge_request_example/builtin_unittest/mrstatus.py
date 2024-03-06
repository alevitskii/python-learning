from enum import StrEnum, auto


class MergeRequestStatus(StrEnum):
    APPROVED = auto()
    REJECTED = auto()
    PENDING = auto()


class MergeRequestExtendedStatus(StrEnum):
    APPROVED = auto()
    REJECTED = auto()
    PENDING = auto()
    OPEN = auto()
    CLOSED = auto()


class MergeRequestException(Exception):
    """Something went wrong with the merge request."""
