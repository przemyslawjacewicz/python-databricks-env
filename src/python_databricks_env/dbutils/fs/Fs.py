import shutil
from pathlib import Path

from python_databricks_env.dbutils.fs.FileInfo import FileInfo
from python_databricks_env.dbutils.fs.MountInfo import MountInfo


class Fs:

    @staticmethod
    def cp(source: str, dest: str, recurse: bool = False) -> bool:
        source_path = Path(source)

        if not source_path.exists():
            raise FileNotFoundError(source)

        if source_path.is_file():
            source_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(source, dest)
            return True

        if source_path.is_dir():
            if not recurse:
                raise Exception("Cannot copy directory unless recurse is set to true")

            shutil.copytree(source, dest, dirs_exist_ok=True)
            return True

        return False

    @staticmethod
    def head(file: str, max_bytes: int = 65536) -> str:
        with open(file, 'rb') as f:
            return f.read(max_bytes).decode('utf-8', errors='ignore')

    @staticmethod
    def ls(path: str) -> list[FileInfo]:
        path_path = Path(path)
        if path_path.is_file():
            return [FileInfo(str(path_path))]
        else:
            return [FileInfo(str(p)) for p in path_path.iterdir()]

    @staticmethod
    def mkdirs(dir: str) -> bool:
        Path(dir).mkdir(parents=True, exist_ok=True)
        return True

    @staticmethod
    def mount(
            source: str,
            mount_point: str,
            encryption_type: str = '',
            owner: str = None,
            extra_configs: dict[str, str] = None
    ) -> bool:
        pass

    @staticmethod
    def mounts() -> list[MountInfo]:
        pass

    @staticmethod
    def mv(source: str, dest: str, recurse: bool = False) -> bool:
        pass

    @staticmethod
    def put(file: str, contents: str, overwrite: bool = False) -> bool:
        file_path = Path(file)

        if file_path.exists() and not overwrite:
            raise Exception(f"File already exists: {file}")

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(contents)

        return True

    @staticmethod
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

    def unmount(mount_point: str) -> bool:
        pass
