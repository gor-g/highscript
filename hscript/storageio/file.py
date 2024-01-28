import os
from hscript.types import Path


def remove(path: Path, nexist_ok: bool = False) -> None:
    if not os.path.exists(path):
        if nexist_ok:
            return
        else:
            raise FileNotFoundError("File not found: {}. Set nexist_ok = True to ignore this kind of errors.".format(path))
    os.remove(path, dir_fd=None)