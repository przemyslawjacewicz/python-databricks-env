import shutil
from pathlib import Path

from pythondatabricksenv.dbutils.fs.FileInfo import FileInfo


def cp(from_: str, to: str, recurse: bool = False) -> bool:
    from_path = Path(from_)

    if from_path.is_file():
        from_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(from_, to)
        return True

    if from_path.is_dir():
        if not recurse:
            raise Exception("Cannot copy directory unless recurse is set to true")

        shutil.copytree(from_, to, dirs_exist_ok=True)
        return True

    return False


def head(file: str, maxBytes: int = 65536) -> str:
    with open(file, 'rb') as f:
        return f.read(maxBytes).decode('utf-8', errors='ignore')


def ls(dir: str) -> list[FileInfo]:
    dir_path = Path(dir)
    if dir_path.is_file():
        return FileInfo.apply(dir_path)
    else:
        return [FileInfo.apply(p) for p in dir_path.iterdir()]


def mkdirs(dir: str) -> bool:
    Path(dir).mkdir(parents=True, exist_ok=True)
    return True


def mv(from_: str, to: str, recurse: bool = False) -> bool:
    pass


def put(file: str, contents: str, overwrite: bool = False) -> bool:
    file_path = Path(file)

    if file_path.exists() and not overwrite:
        raise Exception(f"File already exists: {file}")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(contents)

    return True


def rm(dir: str, recurse: bool = False) -> bool:
    dir_path = Path(dir)

    if not dir_path.exists():
        return False

    if dir_path.is_file():
        dir_path.unlink()
        return True

    if dir_path.is_dir() and recurse:
        shutil.rmtree(dir_path)
        return True
    elif dir_path.is_dir():
        dir_path.rmdir()
        return True

    return False
