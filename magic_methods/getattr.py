# Python first checks the dict for presense of of the attr using __getattribute__
# if not found, calls __getattr__ with attr name
class DynamicAttributes:

    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        # have to raise AttributeError to let the default value be returned
        raise AttributeError(f"{self.__class__.__name__} has no attribute {attr}")


def main() -> None:
    dyn = DynamicAttributes("value")
    print(dyn.attribute)
    print(dyn.fallback_test)

    dyn.__dict__["fallback_new"] = "new value"
    # the call below doesn't get to __getattr__ because __getattribute__ finds it first
    print(dyn.fallback_new)
    print(getattr(dyn, "something", "default"))


# this is called when you access attributes of an imported module
# for example, import <package> and then <package>.<attr> will return
# 'unknown: <attr>' if <attr> is not defined (should throw an error usually)
# when you implement __getattr__ it's recommended to implement __dir__ as well
def __getattr__(attr):
    return f"unknown: {attr}"


# assuming 'foo' is the only attr that getattr will provide
# if it's dynamic then things get complicated
def __dir__():
    return list(globals()) + ["foo"]


if __name__ == "__main__":
    main()
