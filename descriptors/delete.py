from __future__ import annotations

from typing import ClassVar


class ProtectedAttribute:
    def __init__(
        self,
        requires_role: str | None = None,
        name: str = "",
    ) -> None:
        self._permission_required = requires_role
        # it's a good practive to have a default name for compatibility
        # __set_name__ was introduced in 3.6
        self._name = name

    def __set_name__(self, owner: type[User], name: str) -> None:
        self._name = self._name or name

    def __set__(self, user: User, value: object) -> None:
        if value is None:
            raise ValueError(f"{self._name} can't be set to None")
        # can't use setattr because it'll trigger an infinite recursion
        vars(user)[self._name] = value

    def __delete__(self, user: User) -> None:
        if self._permission_required in user.permissions:
            vars(user)[self._name] = None
        else:
            raise ValueError(
                f"User {user!s} doesn't have {self._permission_required} permission"
            )


class User:
    """Only users with "admin" privileges can remove their email address."""

    email: ClassVar = ProtectedAttribute(requires_role="admin")

    def __init__(
        self,
        username: str,
        email: str,
        permission_list: list[str] | None = None,
    ) -> None:
        self.username = username
        self.email = email  # type: ignore
        self.permissions = permission_list or []

    def __str__(self) -> str:
        return self.username


def main() -> None:
    admin = User("root", "root@d.com", ["admin"])
    user = User("user", "user1@d.com", ["email", "helpdesk"])

    print(User.email._name)
    print(admin.email)

    del admin.email
    print(admin.email is None)
    print(user.email)

    # NOTE: Uncomment the following one by one to see the generated errors
    # user.email = None
    # del user.email


if __name__ == "__main__":
    main()
