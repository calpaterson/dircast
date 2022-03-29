from dircast.files import FileMetadata


def pytest_assertrepr_compare(op, left, right):
    if (
        isinstance(left, FileMetadata)
        and isinstance(right, FileMetadata)
        and op == "=="
    ):
        return [
            "Comparing FileMetadata instances:",
            "   vals: %s != %s" % (vars(left), vars(right)),
        ]
