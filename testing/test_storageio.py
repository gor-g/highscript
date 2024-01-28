from faker import Faker
import os
import pytest
from hscript import write, read, append, append_line, read_lines, remove

fake = Faker()

def test_read(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    
    s = fake.sentence()
    with open(path, 'w') as f:
        f.write(s)
    assert read(path) == s

    os.remove(path)
    with open(path, 'w') as f:
        f.write("")
    assert read(path) == ""

    os.remove(path)
    with pytest.raises(FileNotFoundError):
        read(path)



def test_write(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    
    s = fake.sentence()
    write(s, path)
    assert read(path) == s

    with pytest.raises(FileExistsError):
        write(s, path)
    
    with pytest.raises(FileExistsError):
        write(s, path, overwrite=False)

    s = fake.sentence()
    write(s, path, overwrite=True)
    assert read(path) == s

    os.remove(path)


def test_append_line(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    cumul_s = []
    for i in range(10):
        s = fake.sentence()
        append_line(s, path)
        cumul_s.append(s)
    assert read(path) == '\n'.join(cumul_s)
    os.remove(path)

def test_append(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    cumul_s = ""
    for i in range(10):
        s = fake.sentence()
        append(s, path)
        cumul_s += s
    assert read(path) == cumul_s
    os.remove(path)

def test_read_lines(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    cumul_s = []
    for i in range(10):
        s = fake.sentence()
        append_line(s, path)
        cumul_s.append(s)
    assert read_lines(path) == cumul_s
    os.remove(path)


    with open(path, 'w') as f:
        f.write("")
    assert read_lines(path) == ['']
    os.remove(path)


def test_remove(tmp_path):
    path = tmp_path / "test.txt"
    if os.path.exists(path):
        os.remove(path)
    
    with pytest.raises(FileNotFoundError):
        remove(path)
    
    remove(path, nexist_ok=True)

    with open(path, 'w') as f:
        f.write("")
    remove(path)

    assert not os.path.exists(path)