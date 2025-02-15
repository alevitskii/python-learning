from dataclasses import dataclass


class BaseResolverMixin:
    def __getattr__(self, attr: str) -> object:
        if attr.startswith("resolve_"):
            *_, actual_attr = attr.partition("resolve_")
        else:
            actual_attr = attr
        try:
            return vars(self)[actual_attr]
        except KeyError as e:
            raise AttributeError from e


@dataclass
class Customer(BaseResolverMixin):
    customer_id: str
    name: str
    address: str


# a better alternative
def _resolver_method[T](self: T, attr: str) -> object:
    """The resolution method of attributes that will replace __getattr__."""
    if attr.startswith("resolve_"):
        *_, actual_attr = attr.partition("resolve_")
    else:
        actual_attr = attr
    try:
        return vars(self)[actual_attr]
    except KeyError as e:
        raise AttributeError from e


def with_resolver[T](cls: type[T]) -> type[T]:
    """Set the custom resolver method to a class."""
    setattr(cls, "__getattr__", _resolver_method)
    return cls


@with_resolver
@dataclass
class Customer2:
    customer_id: str
    name: str
    address: str


def main() -> None:
    customer = Customer("1", "name", "address")
    print(customer.resolve_customer_id)
    print(customer.resolve_name)

    customer2 = Customer2("1", "name", "address")
    print(customer2.resolve_customer_id)  # type: ignore
    print(customer2.resolve_name)  # type: ignore


if __name__ == "__main__":
    main()
