from typing import NoReturn, Any


class Notebook:

    @staticmethod
    def exit(value: Any) -> NoReturn:
        pass

    @staticmethod
    def run(path: str, timeout_seconds: int, arguments: dict[str, Any] | None = None, *args, **kwargs):
        pass
