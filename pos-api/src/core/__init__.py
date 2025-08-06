import os


def get_version() -> str:
    if "KMPOS_VERSION" in os.environ and len(os.environ["KMPOS_VERSION"]) > 1:
        return os.environ["KMPOS_VERSION"]
    return "unknown"


