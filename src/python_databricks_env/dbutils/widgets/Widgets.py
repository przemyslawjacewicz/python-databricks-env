class Widgets:

    def __init__(self, widgets=None):
        if widgets is None:
            widgets = {}
        self._widgets = widgets

    @staticmethod
    def combobox(name: str, defaultValue: str, choices: list[str], label: str | None = None) -> None:
        pass

    @staticmethod
    def dropdown(name: str, defaultValue: str, choices: list[str], label: str | None = None) -> None:
        pass

    def get(self, name: str) -> str:
        if name in self._widgets:
            return self._widgets[name]
        else:
            raise Exception(f"No input widget named {name} is defined")

    def getAll(self) -> dict[str, str]:
        return self._widgets

    def getArgument(self, name: str, defaultValue: str | None = None) -> str:
        return self._widgets.get(name, defaultValue)

    @staticmethod
    def multiselect(name: str, defaultValue: str, choices: list[str], label: str | None = None) -> None:
        pass

    @staticmethod
    def remove(name: str) -> None:
        pass

    @staticmethod
    def removeAll() -> None:
        pass

    @staticmethod
    def text(name: str, defaultValue: str, label: str | None = None) -> None:
        pass
