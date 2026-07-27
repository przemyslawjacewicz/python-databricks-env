from pathlib import Path


class FileInfo:

    def __init__(self, path: str, name: str, size: int, modificationTime: int):
        self.path = path
        self.name = name
        self.size = size
        self.modificationTime = modificationTime

    # todo: implement me
    def isDir(self) -> bool:
        pass

    # todo: implement me
    def isFile(self) -> bool:
        pass

    # todo: can I name it call and avoid writing the name ?
    @classmethod
    def apply(cls, path: Path):
        return cls(
            path=str(path),
            name=path.name,
            size=path.stat().st_size if not path.is_dir() else 0,
            modificationTime=path.stat().st_mtime
        )
