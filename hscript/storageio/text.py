import os
from typing import List
from hscript.types import Path



def write(s: str, path: Path, overwrite: bool = False) -> None:
    if not overwrite:
        if os.path.exists(path):
            raise FileExistsError("File already exists: {}. Set overwrite = True to overwrite the file, or consider using append() or append_line().".format(path))
    with open(path, 'w') as f:
        f.write(s)

def write_lines(lines: List[str], path: Path) -> None:
    with open(path, 'w') as f:
        f.writelines(lines)

def append(s: str, path: Path) -> None:
    """Append a string to a file. The newline character needs to be included in the string."""
    with open(path, 'a+') as f:
        f.write(s)

def append_line(s: str, path: Path) -> None:
    with open(path, 'a+') as f:
        if os.stat(path).st_size > 0:
            f.write('\n')
        f.write(s)

def read(path: Path) -> str:
    with open(path, 'r') as f:
        return f.read()

def read_lines(path: Path) -> List[str]:
    """if the file is empty returns ['']"""
    # if we were to return an empty list, but if there are two empty lines we 
    # returned ['',''] that would be ambiguous omitting empty lines is also ambiguous
    
    # don't use f.readlines(), it keeps the newline character. 
    # Removing those is slower than just splitting.
    lines = read(path).split('\n')
    return lines
